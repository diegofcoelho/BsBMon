# testSerialSimulator.py
# D. Thiebaut
# This program energizes the fakeSerial simulator using example code taken
# from http://pyserial.sourceforge.net/shortintro.html
# http://cs.smith.edu/dftwiki/index.php/PySerial_Simulator

# import the simulator module (it should be in the same directory as this program)
import binascii

import time

import FakeSerial as serial
import cherrypy


# Example 1  from http://pyserial.sourceforge.net/shortintro.html
def Example1():
    ser = serial.Serial(0)  # open first serial port
    print(ser.name)  # check which port was really used
    ser.write("hello")  # write a string
    ser.close()  # close port


# Example 2  from http://pyserial.sourceforge.net/shortintro.html
def Example2():
    ser = serial.Serial('/dev/ttyS1', 9600, timeout=1)
    x = ser.read()  # read one byte
    print("x = ", x)
    s = ser.read(10)  # read up to ten bytes (timeout)
    print("s = ", s)
    # line = ser.readline()  # read a '\n' terminated line
    # ser.close()
    # print("line = ", line)


# Example 3  from http://pyserial.sourceforge.net/shortintro.html
def Example3():
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 0
    print(ser)

    ser.open()
    print(str(ser.isOpen()))

    ser.close()
    print(ser.isOpen())


def Example4():
    ser = serial.Serial()
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
            return ch
        time.sleep(6)


# Example1()
# Example2()
# Example3()
class Root(object):
    @cherrypy.expose
    def index(self):
        return Example4()

if __name__ == '__main__':
   cherrypy.quickstart(Root(), '/')

