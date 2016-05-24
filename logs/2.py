import serial
import serial.tools.list_ports
import binascii

# http://docs.cherrypy.org/en/latest/advanced.html
# https://github.com/Lawouach/WebSocket-for-Python
# http://srchea.com/build-a-real-time-application-using-html5-websockets
# http://stackoverflow.com/questions/15846684/cherrypy-real-time-web-application
# http://stackoverflow.com/questions/31922175/how-to-stream-data-with-cherrypy
# https://github.com/Lawouach/WebSocket-for-Python
# http://srchea.com/build-a-real-time-application-using-html5-websockets
# https://blog.webfaction.com/2014/05/fun-with-websocket-setting-up-a-shared-drawing-board/
# http://docs.cherrypy.org/en/latest/basics.html#dealing-with-json

ports = [i[0] for i in list(serial.tools.list_ports.comports())]

print(ports)

port = ports[0]  # single/first serial port
ser = serial.Serial(port,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.SEVENBITS, baudrate=9600, parity='N', timeout=0.2)  # opens, too.
print("Monitoring serial port " + ser.name)
data = []
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

