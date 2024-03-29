# -*- coding: utf-8 -*-

# http://www.html5rocks.com/en/tutorials/eventsource/basics/
# http://neokannon.blogspot.com.br/2011/07/cherrypy-server-sent-events-and-you.html
# https://nelsonslog.wordpress.com/2012/12/30/playing-with-websockets/
# http://www.html5rocks.com/en/tutorials/eventsource/basics/
# https://www.000webhost.com/
# http://stackoverflow.com/questions/3473639/best-way-to-convert-string-to-array-of-object-in-javascript
# http://www.carlissongaldino.com.br/post/um-tutorial-passo-passo-para-sqlite-em-python
# http://zetcode.com/db/sqlitepythontutorial/
# https://github.com/daniel-nagy/md-data-table
####################################################################################################
# http://tools.cherrypy.org/wiki/AuthenticationAndAccessRestrictions
####################################################################################################
# http://n3-charts.github.io/line-chart/#/home
# http://www.ng-newsletter.com/posts/d3-on-angular.html
# https://github.com/diegofcoelho/angular-chart.js
# http://jtblin.github.io/angular-chart.js/
# https://github.com/n3-charts/line-chart/wiki/Options
####################################################################################################
import ast
import binascii
import os.path
import random
import sqlite3
import sys
import time
import webbrowser
from multiprocessing import Process

import cherrypy
import serial
import serial.tools.list_ports
from jinja2 import Environment, FileSystemLoader

import FakeSerial as Serial
from auth import AuthController, require
from auth import member_of

current_dir = os.path.dirname(os.path.abspath(__file__))
db = "conf/biostat.db"

wkdir = os.path.abspath(os.path.dirname(__file__))
# sys.exit(print(wkdir))
viewLoader = FileSystemLoader(os.path.join(wkdir, "templates"))
env = Environment(loader=viewLoader)

project = {}
raw = []


class RestrictedArea:
    # all methods in this controller (and subcontrollers) is
    # open only to members of the admin group

    _cp_config = {
        'auth.require': [member_of('admin')]
    }

    @cherrypy.expose
    def index(self):
        return """This is the admin only area."""


class WareHouse:
    def __init__(self):
        self.code = "{'time': '7:41', 'level': '0', 'subs2': '0', 'subs2t': '0.0', 'afoam': '0', 'subs1': '0.0', " \
                    "'temp': '26.1', 'rotation': '0', 'airflow': '0.00', 'base': '0', 'po2': '0.0', 'subs1t': '0', " \
                    "'ph': '7.34', 'acid': '0', 'gasmx': '0.0', 'FLHOEIMV': '0.0', 'lux': '0.0'}"
        if os.path.isfile(db):
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
        else:
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE TABLE runtime (data);")
            a = 'INSERT INTO runtime VALUES ("{}");'.format(self.code)
            self.cursor.execute(a)
            self.conn.commit()
            self.get()

    @staticmethod
    def set(run_vars):
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        sql = 'UPDATE runtime SET data = "{}"'.format(run_vars)
        cursor.execute(sql)
        conn.commit()
        conn.close()

    @staticmethod
    def get():
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        sql = "SELECT * FROM runtime;"
        cursor.execute(sql)
        a = cursor.fetchone()[0]
        conn.close()
        return a  # ou use fetchone()

    @staticmethod
    def generic(sql):
        conn, ans = "", ""
        try:
            conn = sqlite3.connect(db)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            ans = cursor.fetchall()
        except Exception as e:
            raise e
        finally:
            conn.close()
            return ans


def container(data):
    with open('data_container.bbm', 'w') as file_:
        file_.write(str(data))


class Fake232(object):
    def __init__(self):
        self.wh = WareHouse()

    def run(self):
        ser = Serial.Serial()
        data = []
        while True:
            ch = ser.read()
            if len(ch) == 0:
                # rec'd nothing print all
                if len(data) > 0:
                    s = ''
                    for x in data:
                        s += '%02X' % ord(x)
                        # print('%s [len = %d]' % (s, len(data)))
                        # print(str(binascii.a2b_hex(s), "ascii"))
                data = []
            else:
                data.append(ch)
                temp = monitor_vars(str(binascii.a2b_hex(ch), "ascii").replace('\r\n', ''))
                self.wh.set(temp)
            time.sleep(random.randrange(150, 300, random.randrange(1, 10, 1)) / 10)


class Rs232(object):
    def __init__(self):
        self.wh = WareHouse()

    def run(self):
        # Get list with all available prots
        ports = [i[0] for i in list(serial.tools.list_ports.comports())]
        # Show available ports
        print(ports)
        # Choose Port to be used
        port = 'COM3'  # single/first serial port
        # Open ports
        ser = serial.Serial(port,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.SEVENBITS, baudrate=9600, parity='N', timeout=0.2)  # opens, too.
        # Show monitoring message
        print("Monitoring serial port " + ser.name)
        #
        data = []
        #
        while True:
            ch = ser.read(1)
            if len(ch) == 0:
                # rec'd nothing print all
                if len(data) > 0:
                    s = ''
                    for x in data:
                        s += '%02X' % ord(x)
                    # print('%s [len = %d]' % (s, len(data)))
                    temp = monitor_vars(str(binascii.a2b_hex(s), "ascii"))
                    if temp is not None and temp != "None":
                        self.wh.set(temp)
                data = []
            else:
                data.append(ch)


class Root(object):
    # Our toggle variable.
    wh = WareHouse()
    auth = AuthController()
    restricted = RestrictedArea()
    project = {}
    logger = False

    # global USERS
    # USERS = {u[0]: u[1] for u in wh.generic("select `user`, `pwd` FROM `users`")}

    def user_content(self, user):
        #
        ans = {}
        #
        sql_pns = 'SELECT `index`, `id`, `series` FROM projects WHERE user = "{}"'.format(user)
        res_1 = self.wh.generic(sql_pns)
        ans_pns = {i[0]: {i[1]: i[2]} for i in res_1}
        user_projects = list(set(i[1] for i in res_1))
        #
        ans_data = {}
        sql_data = 'SELECT * FROM data'
        res_2 = self.wh.generic(sql_data)
        res = [r for r in res_2 if r[2] in user_projects]
        res_projects = [i[2] for i in res]
        res_series = [i[3] for i in res]
        #
        for i in res_projects:
            ans_data[i] = {}
            for j in res_series:
                ans_data[i][j] = {k[0]: k[4:len(k)] for k in res if j == k[3]}
        #
        ans['projects'] = ans_pns
        ans['data'] = ans_data
        return ans
        #

    @require()
    @cherrypy.expose
    def index(self):
        # cherrypy.session.clear()
        # cherrypy.session.load()
        project['user'] = cherrypy.request.login
        #
        user_data = self.user_content(project['user'])
        #
        # project['id'] = 'Project MicroAlgae'
        # series come as a suggestion based on the number of series for each project
        # project['series'] = 'Series {}'.format(
        #    len([list(set(i.values()))[0] for i in user_data['projects'].values()]) + 1)
        #
        tmpl = env.get_template("BioStatBMD.html")
        return tmpl.render(project=project, udata=user_data)
        # return serve_file(os.path.join(current_dir, 'BioStatBMD.html'), content_type='text/html')
        # return serve_file(os.path.join(current_dir, 'index.html'), content_type='text/html')
        # serves our index client page.

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def time_switch(self):
        # When this page gets requested, it'll toggle the time feed updating
        # and return an OK message.
        if self.timeFeedEnabled:
            self.timeFeedEnabled = False
        else:
            self.timeFeedEnabled = True
        return "Feed Toggled"

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def log(self):
        input_json = cherrypy.request.json
        self.logger = input_json['logger']
        self.project = input_json['project']
        return "Data now is being collected."

    @cherrypy.expose
    def feed(self):
        cherrypy.response.headers["Content-Type"] = "text/event-stream;charset=utf-8"
        data = self.wh.get()
        data_dict = ast.literal_eval(data)
        if self.logger:
            #
            date = time.strftime('%Y-%m-%d %H:%M:%S')
            #
            data_dict['date'] = str(date)
            data_dict['user'] = self.project["user"]
            data_dict['project'] = self.project["id"]
            data_dict['series'] = self.project["series"]
            #
            fields = [f for f in data_dict.keys() if f not in ['time']]
            #
            fields_s = ', '.join(fields)
            values = ['"{}"'.format(data_dict[g]) for g in fields]
            values_s = ', '.join(values)
            # print(fields_s, values_s)
            sql = 'INSERT INTO data ({}) VALUES ({});'.format(fields_s, values_s)
            stat = self.wh.generic(sql)
            #
            #
            #
        else:
            pass
        return "retry: 30000\nevent: time\n" + "data: " + data + "\n\n;"

    feed._cp_config = {'response.stream': True, 'tools.encode.encoding': 'utf-8'}


def monitor_vars(i):
    keys = ["time", "temp", "rotation", "ph", "po2", "acid", "base", "afoam", "level",
            "subs1t", "subs1", "subs2", "subs2t", "gasmx", "airflow", "FLHOEIMV", "lux"]
    res = dict.fromkeys(keys, '0.00')
    #
    raw.append(str(binascii.b2a_hex(bytes(i, "ascii")), "ascii"))
    container(raw)
    #
    if i is not None and i != "None":
        if all(s in i for s in ["|", "."]) and "-" not in i:
            #
            j = i.split("\n")
            for k in j:
                if "|" in k:
                    values = i.replace(" ", "").split("|")
                    # TODO ADD LUX VALUE
                    values.append('0.0')
                    #
                    for e in keys:
                        res[e] = values[keys.index(e)]
                        if res[e] == '000':
                            res[e] = '0.0'
                    return str(res)
                else:
                    alert_msg = k
                    print("An alert message was issued: {}".format(alert_msg))
    else:
        return None


conf = {'/': {
    'tools.sessions.on': True,
    'tools.sessions.timeout': 60,
    'tools.auth.on': True},
    '/public': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, "public")},
    '/fonts': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, "fonts")},
    '/table': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, "table")},
    '/templates': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, "templates")}
}

if __name__ == '__main__':
    ####################################################################################################################
    # if no argument was passed, halt script
    if len(sys.argv) <= 1:
        print("The script will try to connect to your BioStat-B Device.")
        source = None
    elif len(sys.argv) == 2:
        # otherwise parse the argument
        print("The script will try to connect to a Dummy BioStat-B Device.")
        source = sys.argv[1]
    else:
        sys.exit("The script execution was halt because an incorrect number of arguments was passed.")
    ####################################################################################################################
    if source == "Dev":
        rs = Fake232()
        p1 = Process(target=rs.run)
        p1.start()
    else:
        rs = Rs232()
        p1 = Process(target=rs.run)
        p1.start()
    pageroot = Root()
    # And, standard cherrypy quickstart.
    url = 'http://127.0.0.1:8080'
    webbrowser.open(url)
    #
    cherrypy.quickstart(pageroot, config=conf)
