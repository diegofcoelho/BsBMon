# -*- coding: utf-8 -*-
# http://www.html5rocks.com/en/tutorials/eventsource/basics/
# http://neokannon.blogspot.com.br/2011/07/cherrypy-server-sent-events-and-you.html
# https://nelsonslog.wordpress.com/2012/12/30/playing-with-websockets/
# http://www.html5rocks.com/en/tutorials/eventsource/basics/
# https://www.000webhost.com/
# http://stackoverflow.com/questions/3473639/best-way-to-convert-string-to-array-of-object-in-javascript
# http://www.carlissongaldino.com.br/post/um-tutorial-passo-passo-para-sqlite-em-python
# http://zetcode.com/db/sqlitepythontutorial/
import binascii
import os.path
import sqlite3
from multiprocessing import Process

import cherrypy
import serial
import serial.tools.list_ports
import sys

import FakeSerial as Serial
from cherrypy.lib.static import serve_file

current_dir = os.path.dirname(os.path.abspath(__file__))
db = "conf/biostat.db"


class WareHouse:
    def __init__(self):
        self.code = "{'time': '7:41', 'level': '0', 'subs2': '0', 'subs2t': '0.0', 'afoam': '0', 'subs1': '0.0', " \
                    "'temp': '26.1', 'rotation': '0', 'airflow': '0.00', 'base': '0', 'po2': '0.0', 'subs1t': '0', " \
                    "'ph': '7.34', 'acid': '0', 'gasmx': '0.0'}"
        if os.path.isfile(db):
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
        else:
            self.conn = sqlite3.connect(db)
            self.cursor = self.conn.cursor()
            self.cursor.execute("CREATE TABLE runtime (data);")
            a = 'INSERT INTO runtime VALUES ("%s");' % self.code
            self.cursor.execute(a)
            self.conn.commit()
            self.get()

    @staticmethod
    def set(run_vars):
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        sql = 'UPDATE runtime SET data = "%s"' % run_vars
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
                    print(str(binascii.a2b_hex(s), "ascii"))
                data = []
            else:
                data.append(ch)
                temp = MonitorVars(str(binascii.a2b_hex(ch), "ascii"))
                self.wh.set(temp)


class Rs232(object):
    def __init__(self):
        self.wh = WareHouse()

    def run(self):
        # Get list with all available prots
        ports = [i[0] for i in list(serial.tools.list_ports.comports())]
        # Show available ports
        print(ports)
        # Choose Port to be used
        port = ports[0]  # single/first serial port
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
                    temp = MonitorVars(str(binascii.a2b_hex(s), "ascii"))
                    if temp is not None and temp != "None":
                        self.wh.set(temp)
                data = []
            else:
                data.append(ch)


class Root(object):
    # Our toggle variable.
    wh = WareHouse()
    timeFeedEnabled = True

    @cherrypy.expose
    def index(self):
        return serve_file(os.path.join(current_dir, 'BioStatBMD.html'), content_type='text/html')
        # return serve_file(os.path.join(current_dir, 'index.html'), content_type='text/html')
        # serves our index client page.

    @cherrypy.expose
    def timeSwitch(self):
        # When this page gets requested, it'll toggle the time feed updating
        # and return an OK message.
        if self.timeFeedEnabled:
            self.timeFeedEnabled = False
        else:
            self.timeFeedEnabled = True
        return "Feed Toggled"

    @cherrypy.expose
    def sendTime(self):
        # Set the expected headers...
        cherrypy.response.headers["Content-Type"] = "text/event-stream"
        if self.timeFeedEnabled:
            # angular.element($0).parent().scope().data
            # return "event: time\n" + "data: " + self.Example4() + "\n\n;"
            return "event: time\n" + "data: " + self.wh.get() + "\n\n;"
        else:
            pass


def MonitorVars(i):
    res = {}
    if i is not None and i != "None":
        if all(s in i for s in ["|", "."]) and "-" not in i:
            keys = ["time", "temp", "rotation", "ph", "po2", "acid", "base", "afoam", "level",
                    "subs1t", "subs1", "subs2", "subs2t", "gasmx", "airflow"]  # , "FLHOEIMV"]
            values = i.replace(" ", "").split("|")
            for e in keys:
                res[e] = values[keys.index(e)]
            return str(res)
    else:
        return None


conf = {'/public': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, "public")},
        '/fonts': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, "fonts")}
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
    cherrypy.quickstart(pageroot, config=conf)
