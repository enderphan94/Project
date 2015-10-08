#EnderPhan
# import Raspberry Pi GPIO support into Python environment
import RPi.GPIO as GPIO
# import a sleep function from time module
from time import sleep

led = 18  # GPIO number where the led is connected
blue  = 27
red = 10
green = 22

# Tell the GPIO module to use GPIO numbering used by processor
GPIO.setmode(GPIO.BCM)

# Set GPIO no 18 to output mode
# Set GPIO no 27 to output mode
# Set GPIO no 10 to output mode
# Set GPIO no 22 to output mode
GPIO.setup(led, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

body = """
<a href='/off'>Off</a>
<a href='/red'>Red</a>
<a href='/green'>Green</a>
<a href='/blue'>Blue</a>
<a href='/white'>White</a>
"""
# make_server is used to create this simple python webserver
from wsgiref.simple_server import make_server

# Function that is ran when a http request comes in
def simple_app(env, start_response):

    # set some http headers that are sent to the browser
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
# What did the user ask for?
    if env["PATH_INFO"] == "/red":
        GPIO.output(blue, True)
        GPIO.output(red, False)
        GPIO.output(green, True)
    elif env["PATH_INFO"] == "/white":
        GPIO.output(led, False)
        GPIO.output(blue, False)
        GPIO.output(red, False)
        GPIO.output(green, False)
        print("user asked for /on")
        print("user asked for /blue")
        print("user asked for /red")
        print("user asked for /white")
        print("user asked for /green")

    elif env["PATH_INFO"] == "/off":
        GPIO.output(led, True)
        GPIO.output(blue, True)
        GPIO.output(red, True)
        GPIO.output(green, True)
        print("user asked for /off")
        print("user asked for /bule")
        print("user asked for /red")
        print("user asked for /white")
        print("user asked for /green")

    else:
        print("user asked for something else")
    return body

# Create a small python server
httpd = make_server("", 8000, simple_app)
print "Serving on port 8000..."
print "You can open this in the browser http://192.168.1.xxx:8000 where xxx is your rpi ip aadress"
print "Or if you run this server on your own computer then http://localhost:8000"
httpd.serve_forever()

