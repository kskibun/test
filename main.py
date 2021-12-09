import RPi.GPIO as GPIO
import time
#numeracja pinow (wedlug boarda)
#EDIT 11:03
#kolejny edit
GPIO.setmode(GPIO.BOARD)


GPIO.setup(11, GPIO.IN)

while True:
    print (GPIO.input(11))
    time.sleep(0.5)
    GPIO.input(11)

while GPIO.input(11)==1:
    subprocess.run()
