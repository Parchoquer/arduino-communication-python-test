import serial # type: ignore
import time

port = 'COM7'
baudrate = 9600

try:
    ser = serial.Serial(port, baudrate, timeout=1)
    print(f"Connected {port}")
except serial.SerialException:
    print('connection error, check port')
    exit()

try:
    while True:
        cmd = input()
        if cmd == 'exit':
            print('bye')
            ser.close()
            break
        
        ser.write(cmd.encode())
        time.sleep(2)
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            print(f"data : {data}")
except KeyboardInterrupt:
    print('end of the communication')
    ser.close()