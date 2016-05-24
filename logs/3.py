Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/1.py ====================
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/1.py", line 3, in <module>
    import tkMessageBox
ImportError: No module named 'tkMessageBox'
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/1.py ====================
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/1.py", line 6, in <module>
    ser = serial.Serial(port,9600)
  File "C:\Users\LABAM\AppData\Local\Programs\Python\Python35-32\lib\site-packages\serial\serialwin32.py", line 31, in __init__
    SerialBase.__init__(self, *args, **kwargs)
  File "C:\Users\LABAM\AppData\Local\Programs\Python\Python35-32\lib\site-packages\serial\serialutil.py", line 180, in __init__
    self.open()
  File "C:\Users\LABAM\AppData\Local\Programs\Python\Python35-32\lib\site-packages\serial\serialwin32.py", line 62, in open
    raise SerialException("could not open port %r: %r" % (self.portstr, ctypes.WinError()))
serial.serialutil.SerialException: could not open port 'COM4': PermissionError(13, 'Acesso negado.', None, 5)
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 2, in <module>
    import SerialPortScanWin32
ImportError: No module named 'SerialPortScanWin32'
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 2, in <module>
    import SerialPortScanWin32
ImportError: No module named 'SerialPortScanWin32'
>>> import serial.tools.list_ports
print(list(serial.tools.list_ports.comports()))
SyntaxError: multiple statements found while compiling a single statement
>>> import serial.tools.list_ports
>>> print(list(serial.tools.list_ports.comports()))
[<serial.tools.list_ports_common.ListPortInfo object at 0x02DD9550>, <serial.tools.list_ports_common.ListPortInfo object at 0x02DD9350>]
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 3, in <module>
    for i in list(serial.tools.list_ports.comports()):
AttributeError: module 'serial' has no attribute 'tools'
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
COM4 - Prolific USB-to-Serial Comm Port (COM4)
COM1 - Porta de comunicação (COM1)
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 9, in <module>
    port = pList[0][0] - 1 # single/first serial port
NameError: name 'pList' is not defined
>>> import serial.tools.list_ports
>>> serial.tools.list_ports
<module 'serial.tools.list_ports' from 'C:\\Users\\LABAM\\AppData\\Local\\Programs\\Python\\Python35-32\\lib\\site-packages\\serial\\tools\\list_ports.py'>
>>> serial.tools.list_ports.
SyntaxError: invalid syntax
>>> serial.tools.list_ports.comports
<function comports at 0x0262ED20>
>>> serial.tools.list_ports.comports()
<generator object comports at 0x02645630>
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 5, in <module>
    print(i.split("-"))
AttributeError: 'ListPortInfo' object has no attribute 'split'
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
COM4 - Prolific USB-to-Serial Comm Port (COM4)
COM4
Prolific USB-to-Serial Comm Port (COM4)
USB VID:PID=067B:2303 SER=5 LOCATION=1-1
COM1 - Porta de comunicação (COM1)
COM1
Porta de comunicação (COM1)
ACPI\PNP0501\1
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 11, in <module>
    port = pList[0][0] - 1 # single/first serial port
NameError: name 'pList' is not defined
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 8, in <module>
    port = pList[0][0] - 1 # single/first serial port
NameError: name 'pList' is not defined
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 9, in <module>
    ser = serial.Serial(port, baudrate=1200, parity='E', timeout=0.2) # opens, too.
  File "C:\Users\LABAM\AppData\Local\Programs\Python\Python35-32\lib\site-packages\serial\serialwin32.py", line 31, in __init__
    SerialBase.__init__(self, *args, **kwargs)
  File "C:\Users\LABAM\AppData\Local\Programs\Python\Python35-32\lib\site-packages\serial\serialutil.py", line 180, in __init__
    self.open()
  File "C:\Users\LABAM\AppData\Local\Programs\Python\Python35-32\lib\site-packages\serial\serialwin32.py", line 62, in open
    raise SerialException("could not open port %r: %r" % (self.portstr, ctypes.WinError()))
serial.serialutil.SerialException: could not open port 'COM4': PermissionError(13, 'Acesso negado.', None, 5)
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 9, in <module>
    ser = serial.Serial(port, baudrate=9600, parity='N', timeout=0.2) # opens, too.
  File "C:\Users\LABAM\AppData\Local\Programs\Python\Python35-32\lib\site-packages\serial\serialwin32.py", line 31, in __init__
    SerialBase.__init__(self, *args, **kwargs)
  File "C:\Users\LABAM\AppData\Local\Programs\Python\Python35-32\lib\site-packages\serial\serialutil.py", line 180, in __init__
    self.open()
  File "C:\Users\LABAM\AppData\Local\Programs\Python\Python35-32\lib\site-packages\serial\serialwin32.py", line 62, in open
    raise SerialException("could not open port %r: %r" % (self.portstr, ctypes.WinError()))
serial.serialutil.SerialException: could not open port 'COM4': PermissionError(13, 'Acesso negado.', None, 5)
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 10, in <module>
    prin("Monitoring serial port " + ser.name)
NameError: name 'prin' is not defined
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
 AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D [len = 208]
 8A 8F C2 05 09 D2 B0 CD 06 81 C2 B2 36 A3 C1 D4 09 A0 81 A0 81 A0 81 A0 11 C1 D4 B1 45 4B CD 31 81 B2 B9 B0 2D 15 FF B6 81 A0 E9 B5 EC 8D 8A 8D 8A 8D 8A AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 8D 8A A0 2D D6 C5 81 FC 51 C5 33 03 81 FC A0 1A 2D 26 93 A0 A0 C8 81 A0 F1 A0 CF 16 81 A0 A0 B0 58 46 A0 F1 A0 58 D3 31 81 FC 05 C6 16 CD F1 A0 56 D6 31 06 F1 A0 5A 4D B1 0D F1 A0 5A 4D D3 2C F1 A0 5A 4D B2 0D F1 A0 5A 4D D3 16 F1 A0 2C D3 33 03 F1 A0 B0 26 33 CC F1 A0 0C 31 A0 BE 9C FC A0 87 BA BB 07 F1 A0 E1 C3 81 A0 A0 C9 F0 3B 81 FC 81 F0 06 81 A0 A0 95 A0 81 A0 A0 B5 EC 81 A0 A0 B5 EC 81 A0 A0 B5 EC 81 A0 A0 B5 EC 81 A0 A0 B5 EC 81 A0 A0 95 A0 81 A0 A0 B5 EC 81 A0 A0 95 A0 81 A0 A0 95 A0 81 A0 A0 B1 AF 3B 81 FC 3D A0 31 25 8D 8A AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B A0 33 59 A0 7F E3 F1 [len = 431]
 A0 E1 BA AD 81 FC 81 B2 96 85 81 FC A0 81 B2 C1 A0 A0 DD AE AC 81 FC A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 B0 05 81 FC 81 A0 B9 B0 F1 A0 C1 AE C1 A0 A0 81 B0 C1 8D 8A [len = 87]
 A0 E1 BA 2D 16 F1 A0 C9 B3 85 81 FC A0 81 B2 C1 A0 A0 DD AE 2C 16 F1 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 B0 05 81 FC 81 A0 B9 B0 F1 A0 C1 AE C1 A0 A0 81 B0 C1 8D 8A [len = 87]
 A0 E1 BA AD 16 F1 A0 C9 B3 85 81 FC A0 81 B2 C1 A0 A0 DD AE AC 81 FC A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 B0 05 81 FC 81 A0 B9 B0 F1 A0 C1 AE C1 A0 A0 81 B0 C1 8D 8A [len = 87]
 A0 E1 BA 2D 0B F1 A0 C9 B3 85 81 FC A0 81 B2 C1 A0 A0 DD AE 2C 16 F1 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 B0 05 81 FC 81 A0 B9 B0 F1 A0 C1 AE C1 A0 A0 81 B0 C1 8D 8A [len = 87]
 A0 E1 BA AD 0B F1 A0 C9 B3 85 81 FC A0 81 B2 C1 A0 A0 DD AE 2C 16 F1 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 B0 05 81 FC 81 A0 B9 B0 F1 A0 C1 AE C1 A0 A0 81 B0 C1 8D 8A [len = 87]
 A0 E1 BA 2D 0B F1 A0 C9 B3 85 81 FC A0 81 B2 C1 A0 A0 DD AE 2C 16 F1 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 B0 05 81 FC 81 A0 B9 B0 F1 A0 C1 AE C1 A0 A0 81 B0 C1 8D 8A [len = 87]
 A0 E1 BA AD 0B F1 A0 C9 B3 85 81 FC A0 81 B2 C1 A0 A0 DD AE 2C 16 F1 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 B0 05 81 FC 81 A0 B9 B0 F1 A0 C1 AE C1 A0 A0 81 B0 C1 8D 8A [len = 87]

==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
 AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D 8A 8D [len = 206]
<class 'str'>
 8A 8F C2 05 09 D2 B0 CD 06 81 C2 B2 36 A3 C1 D4 09 A0 81 A0 81 A0 81 A0 11 C1 D4 B1 45 4B CD 31 81 B2 B9 B0 2D 15 FF B6 81 A0 2E 17 D1 8D 8A 8D 8A 8D 8A AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 AD AD AB D5 B5 AD AB D5 B5 AD AB D5 B5 8D 8A A0 2D D6 C5 81 FC 51 C5 33 03 81 FC A0 1A 2D 26 93 A0 A0 C8 81 A0 F1 A0 CF 16 81 A0 A0 B0 58 46 A0 F1 A0 58 D3 31 81 FC 05 C6 16 CD F1 A0 56 D6 31 06 F1 A0 5A 4D B1 0D F1 A0 5A 4D D3 2C F1 A0 5A 4D B2 0D F1 A0 5A 4D D3 16 F1 A0 2C D3 33 03 F1 A0 B0 26 33 CC F1 A0 0C 31 A0 BE 9C FC A0 87 BA BB 07 F1 A0 E1 C3 81 A0 A0 C9 F0 3B 81 FC 81 F0 06 81 A0 A0 95 A0 81 A0 A0 B5 EC 81 A0 A0 B5 EC 81 A0 A0 B5 EC 81 A0 A0 B5 EC 81 A0 A0 B5 EC 81 A0 A0 95 A0 81 A0 A0 B5 EC 81 A0 A0 95 A0 81 A0 A0 95 A0 81 A0 A0 B1 AF 3B 81 FC 3D A0 31 25 8D 8A AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B AD AB D5 B5 AD 2B A0 33 59 A0 7F E3 F1 [len = 431]
<class 'str'>
 A0 E5 BA D1 A0 A0 C9 B3 95 81 FC A0 81 B2 C1 A0 A0 DD AE E5 A0 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 B0 05 81 FC 81 A0 B9 B0 F1 A0 C1 AE C1 A0 A0 81 B0 C1 8D 8A [len = 85]
<class 'str'>
 A0 E5 BA D5 A0 A0 C9 B3 85 81 FC A0 81 B2 C1 A0 A0 DD AE 2C 81 FC A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 A0 C1 A0 A0 81 B0 05 81 FC 81 A0 81 B0 F1 A0 81 B0 05 81 FC 81 A0 B9 B0 F1 A0 C1 AE C1 A0 A0 81 B0 C1 8D 8A [len = 86]
<class 'str'>

==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D [len = 240]
<class 'str'>
 0A 0F 42 2E 20 42 52 41 55 4E 20 20 42 49 4F 53 54 41 54 20 42 20 20 20 20 20 20 20 20 20 20 20 44 41 54 45 2F 54 49 4D 45 20 20 32 30 2E 30 35 2E 31 36 20 20 20 39 3A 30 36 0D 0A 0D 0A 0D 0A 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 20 54 49 4D 45 20 20 7C 20 54 45 4D 50 20 20 7C 20 53 54 49 52 52 20 7C 20 70 48 20 20 20 20 7C 20 70 4F 32 20 20 20 7C 20 41 43 49 44 20 20 7C 20 42 41 53 45 20 20 7C 20 41 46 4F 41 4D 20 7C 20 4C 45 56 45 4C 20 7C 20 53 55 42 31 54 20 7C 20 53 55 42 53 31 20 7C 20 53 55 42 32 54 20 7C 20 53 55 42 53 32 20 7C 20 47 41 53 4D 58 20 7C 20 41 49 52 46 4C 20 7C 20 46 20 4C 20 48 0D 0A 20 68 68 3A 6D 6D 20 7C 20 20 78 43 20 20 20 7C 20 20 72 70 6D 20 20 7C 20 20 70 48 20 20 20 7C 20 20 25 20 20 20 20 7C 20 20 6D 6C 20 20 20 7C 20 20 6D 6C 20 20 20 7C 20 20 6D 6C 20 20 20 7C 20 20 6D 6C 20 20 20 7C 20 20 6D 6C 20 20 20 7C 20 20 25 20 20 20 20 7C 20 20 6D 6C 20 20 20 7C 20 20 25 20 20 20 20 7C 20 20 25 20 20 20 20 7C 20 20 6C 2F 6D 20 20 7C 20 4F 20 45 20 49 0D 0A 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 2D 2D 2D 2D 2D 2D 2D 7C 20 4D 20 56 20 20 0D 0A [len = 577]
<class 'str'>
 20 20 39 3A 30 36 20 7C 20 20 32 33 2E 38 20 7C 20 20 20 32 30 30 20 7C 20 20 37 2E 31 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 30 2E 30 30 20 7C 20 30 20 30 20 30 0D 0A [len = 128]
<class 'str'>
 20 20 39 3A 30 37 20 7C 20 20 32 33 2E 39 20 7C 20 20 20 32 30 30 20 7C 20 20 37 2E 31 31 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 30 2E 30 30 20 7C 20 30 20 30 20 30 0D 0A [len = 128]
<class 'str'>
 20 20 39 3A 30 38 20 7C 20 20 32 33 2E 38 20 7C 20 20 20 32 30 30 20 7C 20 20 37 2E 31 31 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 30 2E 30 30 20 7C 20 30 20 30 20 30 0D 0A [len = 128]
<class 'str'>
 20 20 39 3A 30 39 20 7C 20 20 32 33 2E 39 20 7C 20 20 20 32 30 30 20 7C 20 20 37 2E 30 39 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 30 2E 30 30 20 7C 20 30 20 30 20 30 0D 0A [len = 128]
<class 'str'>
 20 20 39 3A 31 30 20 7C 20 20 32 33 2E 39 20 7C 20 20 20 32 30 30 20 7C 20 20 37 2E 30 39 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 30 2E 30 30 20 7C 20 30 20 30 20 30 0D 0A [len = 128]
<class 'str'>
 20 20 39 3A 31 31 20 7C 20 20 32 33 2E 39 20 7C 20 20 20 32 30 30 20 7C 20 20 37 2E 31 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 30 2E 30 30 20 7C 20 30 20 30 20 30 0D 0A [len = 128]
<class 'str'>
 20 20 39 3A 31 32 20 7C 20 20 32 33 2E 39 20 7C 20 20 20 32 30 30 20 7C 20 20 37 2E 31 31 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 30 2E 30 30 20 7C 20 30 20 30 20 30 0D 0A [len = 128]
<class 'str'>
 20 20 39 3A 31 33 20 7C 20 20 32 33 2E 39 20 7C 20 20 20 32 30 30 20 7C 20 20 37 2E 31 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 20 20 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 20 30 2E 30 20 7C 20 20 30 2E 30 30 20 7C 20 30 20 30 20 30 0D 0A [len = 128]
<class 'str'>

==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 24, in <module>
    print(binascii.a2b_hex(s))
binascii.Error: Non-hexadecimal digit found
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 24, in <module>
    print(binascii.a2b_hex(s))
binascii.Error: Odd-length string
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 22, in <module>
    s +=  ord(x)
TypeError: Can't convert 'int' object to str implicitly
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 24, in <module>
    print(binascii.a2b_hex(s))
binascii.Error: Non-hexadecimal digit found
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 2D 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D 0A 0D [len = 242]
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 24, in <module>
    print(binascii.a2b_hex(s))
binascii.Error: Non-hexadecimal digit found
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
Traceback (most recent call last):
  File "C:/Users/LABAM/Desktop/2.py", line 22, in <module>
    s += '%' % ord(x)
ValueError: incomplete format
>>> 
==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D0A0D [len = 242]
b'-------------------------------------------------------------------------------------------------------------------------------\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r'
0A0F422E20425241554E202042494F5354415420422020202020202020202020444154452F54494D45202032302E30352E3136202020393A31360D0A0D0A0D0A2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D2D0D0A2054494D4520207C2054454D5020207C205354495252207C207048202020207C20704F322020207C204143494420207C204241534520207C2041464F414D207C204C4556454C207C205355423154207C205355425331207C205355423254207C205355425332207C204741534D58207C20414952464C207C2046204C20480D0A2068683A6D6D207C202078432020207C202072706D20207C202070482020207C202025202020207C20206D6C2020207C20206D6C2020207C20206D6C2020207C20206D6C2020207C20206D6C2020207C202025202020207C20206D6C2020207C202025202020207C202025202020207C20206C2F6D20207C204F204520490D0A2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C2D2D2D2D2D2D2D7C204D205620200D0A [len = 577]
b'\n\x0fB. BRAUN  BIOSTAT B           DATE/TIME  20.05.16   9:16\r\n\r\n\r\n-------------------------------------------------------------------------------------------------------------------------------\r\n TIME  | TEMP  | STIRR | pH    | pO2   | ACID  | BASE  | AFOAM | LEVEL | SUB1T | SUBS1 | SUB2T | SUBS2 | GASMX | AIRFL | F L H\r\n hh:mm |  xC   |  rpm  |  pH   |  %    |  ml   |  ml   |  ml   |  ml   |  ml   |  %    |  ml   |  %    |  %    |  l/m  | O E I\r\n-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------| M V  \r\n'
2020393A3136207C202032332E39207C202020323030207C2020372E3131207C202020302E30207C202020202030207C202020202030207C202020202030207C202020202030207C202020202030207C202020302E30207C202020202030207C202020302E30207C202020302E30207C2020302E3030207C2030203020300D0A [len = 128]
b'  9:16 |  23.9 |   200 |  7.11 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0\r\n'
2020393A3137207C202032332E39207C202020323030207C2020372E3131207C202020302E30207C202020202030207C202020202030207C202020202030207C202020202030207C202020202030207C202020302E30207C202020202030207C202020302E30207C202020302E30207C2020302E3030207C2030203020300D0A [len = 128]
b'  9:17 |  23.9 |   200 |  7.11 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0\r\n'

==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
-------------------------------------------------------------------------------------------------------------------------------

























































B. BRAUN  BIOSTAT B           DATE/TIME  20.05.16   9:18


-------------------------------------------------------------------------------------------------------------------------------
 TIME  | TEMP  | STIRR | pH    | pO2   | ACID  | BASE  | AFOAM | LEVEL | SUB1T | SUBS1 | SUB2T | SUBS2 | GASMX | AIRFL | F L H
 hh:mm |  xC   |  rpm  |  pH   |  %    |  ml   |  ml   |  ml   |  ml   |  ml   |  %    |  ml   |  %    |  %    |  l/m  | O E I
-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------| M V  

  9:18 |  23.8 |   200 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0


==================== RESTART: C:/Users/LABAM/Desktop/2.py ====================
['COM4', 'COM1']
Monitoring serial port COM4
-------------------------------------------------------------------------------------------------------------------------------


























































B. BRAUN  BIOSTAT B           DATE/TIME  20.05.16   9:19


-------------------------------------------------------------------------------------------------------------------------------
 TIME  | TEMP  | STIRR | pH    | pO2   | ACID  | BASE  | AFOAM | LEVEL | SUB1T | SUBS1 | SUB2T | SUBS2 | GASMX | AIRFL | F L H
 hh:mm |  xC   |  rpm  |  pH   |  %    |  ml   |  ml   |  ml   |  ml   |  ml   |  %    |  ml   |  %    |  %    |  l/m  | O E I
-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------| M V  

  9:19 |  23.9 |   200 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:20 |  23.8 |   200 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:21 |  23.8 |   200 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:22 |  23.8 |   329 |  7.08 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:23 |  23.9 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:24 |  23.8 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:25 |  23.9 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:26 |  23.9 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:27 |  23.9 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:28 |  23.9 |   330 |  7.11 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:29 |  23.9 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:30 |  23.9 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:31 |  23.9 |   330 |  7.11 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:32 |  23.9 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:33 |  23.9 |   331 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:34 |  23.9 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:35 |  24.0 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:36 |  23.9 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:37 |  24.0 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:38 |  24.0 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:39 |  23.9 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:40 |  23.9 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:41 |  23.9 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:42 |  23.9 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:43 |  23.9 |   329 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:44 |  23.9 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:45 |  23.9 |   330 |  7.11 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:46 |  23.9 |   330 |  7.12 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:47 |  23.9 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:48 |  23.9 |   330 |  7.11 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:49 |  24.0 |   330 |  7.11 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:50 |  24.0 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:51 |  24.0 |   330 |  7.11 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:52 |  24.0 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:53 |  24.0 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:54 |  24.0 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:55 |  24.0 |   330 |  7.10 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:56 |  24.0 |   330 |  7.07 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:57 |  24.0 |   329 |  7.13 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:58 |  24.1 |   330 |  7.12 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

  9:59 |  24.1 |   330 |  7.08 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 10:00 |  24.1 |   330 |  7.08 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 10:01 |  24.1 |   330 |  7.07 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 10:02 |  24.1 |   330 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:36 |  23.8 |   429 |  7.04 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:37 |  23.8 |   430 |  7.05 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:38 |  23.8 |   430 |  7.05 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:39 |  23.8 |   430 |  7.04 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:40 |  23.8 |   431 |  7.03 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:41 |  23.8 |   430 |  7.02 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:42 |  23.8 |   430 |  7.03 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:43 |  23.8 |   430 |  7.02 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:44 |  23.8 |   431 |  7.02 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:45 |  23.8 |   430 |  7.00 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:46 |  23.8 |   430 |  6.99 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:47 |  23.8 |   430 |  6.99 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:48 |  23.8 |   431 |  7.00 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0
-------------------------------------------------------------------------------------------------------------------------------









B. BRAUN  BIOSTAT B           DATE/TIME  20.05.16  11:49


-------------------------------------------------------------------------------------------------------------------------------
 TIME  | TEMP  | STIRR | pH    | pO2   | ACID  | BASE  | AFOAM | LEVEL | SUB1T | SUBS1 | SUB2T | SUBS2 | GASMX | AIRFL | F L H
 hh:mm |  xC   |  rpm  |  pH   |  %    |  ml   |  ml   |  ml   |  ml   |  ml   |  %    |  ml   |  %    |  %    |  l/m  | O E I
-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------| M V  

 11:49 |  23.8 |   431 |  6.99 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:50 |  23.8 |   430 |  7.01 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:51 |  23.8 |   430 |  7.01 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:52 |  23.8 |   430 |  7.00 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:53 |  23.8 |   430 |  6.99 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:54 |  23.8 |   431 |  6.99 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:55 |  23.8 |   431 |  6.99 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:56 |  23.8 |   431 |  6.99 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 11:57 |  23.8 |   429 |  6.99 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0



















































B. BRAUN  BIOSTAT B           DATE/TIME  20.05.16  12:02


-------------------------------------------------------------------------------------------------------------------------------
 TIME  | TEMP  | STIRR | pH    | pO2   | ACID  | BASE  | AFOAM | LEVEL | SUB1T | SUBS1 | SUB2T | SUBS2 | GASMX | AIRFL | F L H
 hh:mm |  xC   |  rpm  |  pH   |  %    |  ml   |  ml   |  ml   |  ml   |  ml   |  %    |  ml   |  %    |  %    |  l/m  | O E I
-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------| M V  
 12:02 |  23.8 |  1200 |  6.99 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:03 |  23.8 |     0 |  7.02 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:04 |  23.8 |     0 |  6.99 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:05 |  23.8 |     0 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:06 |  23.7 |     0 |  7.01 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:07 |  23.7 |     0 |  7.09 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:08 |  23.7 |     0 |  7.08 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:09 |  23.6 |     0 |  7.08 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:10 |  23.6 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:11 |  23.6 |     0 |  7.04 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:12 |  23.5 |     0 |  7.04 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:13 |  23.5 |     0 |  7.03 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:14 |  23.5 |     0 |  7.04 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:15 |  23.5 |     0 |  7.04 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:16 |  23.5 |     0 |  7.03 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:17 |  23.4 |     0 |  7.04 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:18 |  23.4 |     0 |  7.05 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:19 |  23.4 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:20 |  23.4 |     0 |  7.07 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:21 |  23.3 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:22 |  23.3 |     0 |  7.07 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:23 |  23.3 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:24 |  23.2 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:25 |  23.2 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:26 |  23.2 |     0 |  7.04 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:27 |  23.2 |     0 |  7.03 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:28 |  23.1 |     0 |  7.05 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:29 |  23.2 |     0 |  7.05 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:30 |  23.1 |     0 |  7.05 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:31 |  23.1 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:32 |  23.1 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:33 |  23.1 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:34 |  23.0 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:35 |  23.0 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

 12:38 |  23.0 |     0 |  7.06 |   0.0 |     0 |     0 |     0 |     0 |     0 |   0.0 |     0 |   0.0 |   0.0 |  0.00 | 0 0 0

