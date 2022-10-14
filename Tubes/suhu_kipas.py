import pyfirmata
import time

port = 'COM3'

board = pyfirmata.Arduino(port) 

temperature_pin = board.get_pin('a:0:i') 
relay_pin = board.get_pin('d:8:o')
HIGH = True 
LOW = False 
iterator = pyfirmata.util.Iterator(board) 
iterator.start() 
temperature_pin.enable_reporting()  

while temperature_pin.read() == None: 
    None 

try:
    while True: 
        print ("temperature between 0 and 1 :",temperature_pin.read()) 
        Celsius = ((temperature_pin.read()*5 - 0.5) *100)  
        print ("temperature in Celsius :" ,(round(Celsius,4)))
        if Celsius > 32 and Celsius < 45:
            print("Panas cuy, nyalakan dong kipasnya")
            relay_pin.write(HIGH)
        elif Celsius < 32:
            print("Dingin cuy, matikan dong kipasnya")
            relay_pin.write(LOW)
        time.sleep(1)
except:
    temperature_pin.disable_reporting() 
    board.exit( )