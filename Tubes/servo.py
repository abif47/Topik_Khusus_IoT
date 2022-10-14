import pyfirmata
import time

port = 'COM3'
HIGH = True 
LOW = False 
board = pyfirmata.Arduino(port) 
servo_pin = board.get_pin('d:9:s') 
LED_pin = board.get_pin('d:8:o')
Buzzer_pin = board.get_pin('d:10:o')

while True: # Infinite loop
    akses = input("Apakah anda ingin masuk/keluar? ")
    if akses == "Masuk" or akses == "Keluar"  :
        angle = 70
        servo_pin.write(angle)
        LED_pin.write(HIGH)
        time.sleep(10)
        angle = 0
        servo_pin.write(angle)
        LED_pin.write(LOW)
    else:
        Buzzer_pin.write(HIGH) 
        time.sleep(0.5) 
        Buzzer_pin.write(LOW) 
        time.sleep(0.5) 