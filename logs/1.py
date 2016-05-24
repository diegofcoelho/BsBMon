import serial
#from Tkinter import *
#import tkMessageBox

port = "COM4"
ser = serial.Serial(port,9600)
value = 0


while 1:
    value = ser.read()
    print(value)
