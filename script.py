#!/bin/python3
import os
import time
from gpiozero import Button, LED
from datetime import datetime
from signal import pause
import socket

button18 = Button(18)
button23 = Button(23)

db_host = "20.107.176.118"
db_port = 3306
db_user = "iot2023_device"
db_password = "iot2023_device"
db_name = "iot_db"

def take_photo(trigger_sensor):
    now = datetime.now()
    current_time = now.strftime("%d%m%y-%H-%M")
    os.system(f"libcamera-jpeg -o 1_{current_time}.jpg ")
    print("Photo is sending...")
    os.system(f"scp -i ftp-key.pem 1_{current_time}.jpg  ftp@20.107.176.118:/files")
    print("Photo is sended")

def send_alarm(trigger_sensor):
    s = socket.socket()
    s.connect(('127.0.0.1',8888))
    str = f"{trigger_sensor}"
    s.send(str.encode())
    s.close()

while True:
    if button18.is_pressed:
        print("Button18 is not pressed")
    else:
        take_photo(2)
        send_alarm(2)

    if button23.is_pressed:
        print("Button23 is not pressed")
    else:
        take_photo(3)
        send_alarm(3)

    time.sleep(1)

