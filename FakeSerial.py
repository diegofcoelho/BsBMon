# coding=utf-8
# fakeSerial.py
# D. Thiebaut
# A very crude simulator for PySerial assuming it
# is emulating an Arduino.


# a Serial class emulator
import ast
import random


class Serial:
    # init(): the constructor.  Many of the arguments have default values
    # and can be skipped when calling the constructor.
    def __init__(self, port='COM69', baudrate=9600, timeout=1,
                 bytesize=7, parity='N', stopbits=1, xonxoff=0,
                 rtscts=0):
        self.name = port
        self.port = port
        self.timeout = timeout
        self.parity = parity
        self.baudrate = baudrate
        self.bytesize = bytesize
        self.stopbits = stopbits
        self.xonxoff = xonxoff
        self.rtscts = rtscts
        self._isOpen = True
        self._receivedData = ""
        self._data = "It was the best of times.\nIt was the worst of times.\n"
        self._data = self.container()

    ## isOpen()
    # returns True if the port to the Arduino is open.  False otherwise
    def isOpen(self):
        return self._isOpen

    ## open()
    # opens the port
    def open(self):
        self._isOpen = True

    ## close()
    # closes the port
    def close(self):
        self._isOpen = False

    ## write()
    # writes a string of characters to the Arduino
    def write(self, string):
        print('Arduino got: "' + string + '"')
        self._receivedData += string

    ## read()
    # reads n characters from the fake Arduino. Actually n characters
    # are read from the string _data and returned to the caller.
    def read(self, n=1):
        # s = self._data[0:n]
        s = self._data[random.randint(0, len(self._data) - 1)]
        # self._data = self._data[n:]
        # print( "read: now self._data = ", self._data )
        return s

    # readline()
    # reads characters from the fake Arduino until a \n is found.
    def readline(self):
        returnIndex = self._data.index("\n")
        if returnIndex != -1:
            s = self._data[0:returnIndex + 1]
            self._data = self._data[returnIndex + 1:]
            return s
        else:
            return ""

    ## __str__()
    # returns a string representation of the serial class
    def __str__(self):
        return "Serial<id=0xa81c10, open=%s>( port='%s', baudrate=%d," \
               % (str(self.isOpen), self.port, self.baudrate) \
               + " bytesize=%d, parity='%s', stopbits=%d, xonxoff=%d, rtscts=%d)" \
                 % (self.bytesize, self.parity, self.stopbits, self.xonxoff,
                    self.rtscts)

    @staticmethod
    def container():
        with open('dev/data_container.bbm', 'r') as file_:
            c = ast.literal_eval(file_.read())
            content = [bytes(b, 'utf8') for b in c]
        return content
