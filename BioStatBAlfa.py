# http://www.html5rocks.com/en/tutorials/eventsource/basics/
# http://neokannon.blogspot.com.br/2011/07/cherrypy-server-sent-events-and-you.html
# https://nelsonslog.wordpress.com/2012/12/30/playing-with-websockets/
# http://www.html5rocks.com/en/tutorials/eventsource/basics/
# https://www.000webhost.com/
# http://stackoverflow.com/questions/3473639/best-way-to-convert-string-to-array-of-object-in-javascript
import binascii
import os.path
import time

import cherrypy
import serial
import serial.tools.list_ports
from cherrypy.lib.static import serve_file

import biostat.FakeSerial as Serial

current_dir = os.path.dirname(os.path.abspath(__file__))


class Root(object):
    # Our toggle variable.
    timeFeedEnabled = True

    def __init__(self):
        self.i = ""
        # self.rs232()
        pass

    def rs232(self):
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
                    print(str(binascii.a2b_hex(s), "ascii"))
                data = []
            else:
                data.append(ch)

    def Example4(self):
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
                return str(binascii.a2b_hex(ch), "ascii")

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
            temp = str(MonitorVars(self.Example4()))
            self.i = (self.i, temp)[temp is not None]
            return "event: time\n" + "data: " + self.i + "\n\n;"
        else:
            pass


def MonitorVars(i):
    res = {}
    if all(s in i for s in ["|", "."]) and "-" not in i:
        keys = ["time", "temp", "rotation", "ph", "po2", "acid", "base", "afoam", "level",
                "subs1t", "subs1", "subs2", "subs2t", "gasmx", "airflow"]#, "FLHOEIMV"]
        values = i.replace(" ", "").split("|")
        for e in keys:
            res[e] = values[keys.index(e)]
        return res

conf = {'/public': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, "public")},
        '/fonts': {'tools.staticdir.on': True, 'tools.staticdir.dir': os.path.join(current_dir, "fonts")}
        }

if __name__ == '__main__':
    pageroot = Root()
    # And, standard cherrypy quickstart.
    cherrypy.quickstart(pageroot, config=conf)
