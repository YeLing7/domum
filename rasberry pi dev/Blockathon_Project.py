import RPi.GPIO as GPIO  
import time
import interpreter as a


def button1_pressed():
    input = int(a.getNum(1))
    if input >0:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
        a.sendData(1)
        
def button2_pressed():
    input = int(a.getNum(2))
    if input >0:
        GPIO.output(17, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(17, GPIO.LOW)
        time.sleep(1)
        a.sendData(2)

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    while True:
        input_signal = input('Please press the number of your room: ')
        print(input_signal)
        if input_signal == '1':
            print(a.getNum(1))
            button1_pressed()
        elif input_signal == '2':
            print(a.getNum(2))
            button2_pressed()
        else:
            print('Please enter room number between 1 and 2.')
        
