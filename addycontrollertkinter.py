from Tkinter import *
import RPi.GPIO as GPIO
import os

GPIO.setwarnings = FALSE
GPIO.setmode(GPIO.BOARD)
#WHEELS
Motor1A = 15
Motor1B = 13
Motor1E = 11
 
Motor2A = 36
Motor2B = 38
Motor2E = 40
#ARM
ARM1A = 19
ARM1B = 21
ARM1E = 23
 
ARM2A = 16
ARM2B = 18
ARM2E = 22
#LED
LED = 37

GPIO.setup(LED,GPIO.OUT)
GPIO.setup(ARM1A,GPIO.OUT) 
GPIO.setup(ARM1B,GPIO.OUT) 
GPIO.setup(ARM1E,GPIO.OUT) 
GPIO.setup(ARM2A,GPIO.OUT) 
GPIO.setup(ARM2B,GPIO.OUT) 
GPIO.setup(ARM2E,GPIO.OUT) 

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
 
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)

GPIO.output(Motor1E,GPIO.LOW)
GPIO.output(Motor2E,GPIO.LOW)
GPIO.output(ARM1E,GPIO.LOW)
GPIO.output(ARM2E,GPIO.LOW)

def ledon():
    print "LED ON"
    os.system('mpg123 -q on.mp3 &')
    GPIO.output(LED,GPIO.HIGH)
    
def ledoff():
    print "LED OFF"
    os.system('mpg123 -q off.mp3 &')
    GPIO.output(LED,GPIO.LOW)
    
def armforward():
    print "ARM forwards"
    os.system('mpg123 -q movingarm.mp3 &')
    GPIO.output(ARM1A,GPIO.HIGH)
    GPIO.output(ARM1B,GPIO.LOW)
    GPIO.output(ARM1E,GPIO.HIGH)
    
def armbackward():
    print "ARM backwards"
    os.system('mpg123 -q movingarm.mp3 &')
    GPIO.output(ARM1A,GPIO.LOW)
    GPIO.output(ARM1B,GPIO.HIGH)
    GPIO.output(ARM1E,GPIO.HIGH)
    
def armstop():
    GPIO.output(ARM1E,GPIO.LOW)
    os.system('mpg123 -q stop.mp3 &')
    
def griptight():
    print "GRIP tightining"
    os.system('mpg123 -q movinggrip.mp3 &')
    GPIO.output(ARM2A,GPIO.LOW)
    GPIO.output(ARM2B,GPIO.HIGH)
    GPIO.output(ARM2E,GPIO.HIGH)

def griploose():
    print "GRIP loosing"
    os.system('mpg123 -q movinggrip.mp3 &')
    GPIO.output(ARM2A,GPIO.HIGH)
    GPIO.output(ARM2B,GPIO.LOW)
    GPIO.output(ARM2E,GPIO.HIGH)

def gripstop():
    GPIO.output(ARM2E,GPIO.LOW)
    os.system('mpg123 -q stop.mp3 &')

def forward():
    print "Going forwards"
    os.system('mpg123 -q movingforward.mp3 &')
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
 
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    
def right():
    print "Going right"
    os.system('mpg123 -q turningright.mp3 &')
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
                
    GPIO.output(Motor2E,GPIO.LOW)
    
def left():
    print "Going left"
    os.system('mpg123 -q turningleft.mp3 &')
    GPIO.output(Motor1E,GPIO.LOW)
                
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)

def backward():
    print "Going backward"
    os.system('mpg123 -q movingbackward.mp3 &')
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
 
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    
def clean():
    GPIO.cleanup()
    
def stop():
    print "Now stop"
    os.system('mpg123 -q stop.mp3 &')
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)

def quity():
    print "Quiting"
    os.system('mpg123 -q byeseeyousoon.mp3 &')
    quit

    
root = Tk()
os.system('mpg123 -q pleasewaitstarting.mp3 &')

fw = Button(root, text="FORWARD", bg="green", command=forward)
fw.pack(side=TOP, padx=10, pady=10, ipadx=10, ipady=10)

armfw = Button(root, text="ARM FW", bg="yellow", command=armforward)
armfw.pack(side=TOP, padx=10, pady=10, ipadx=10, ipady=10)

lf = Button(root, text="LEFT", bg="green", command=left)
lf.pack(side=LEFT, padx=10, pady=10, ipadx=10, ipady=10)

griplf = Button(root, text="GRIP L", bg="yellow", command=griploose)
griplf.pack(side=LEFT, padx=10, pady=10, ipadx=10, ipady=10)

rt = Button(root, text="RIGHT", bg="green", command=right)
rt.pack(side=RIGHT, padx=10, pady=10, ipadx=10, ipady=10)

griprt = Button(root, text="GRIP T", bg="yellow", command=griptight)
griprt.pack(side=RIGHT, padx=10, pady=10, ipadx=10, ipady=10)

bk = Button(root, text="BACKWARD", bg="green", command=backward)
bk.pack(side=BOTTOM, padx=10, pady=10, ipadx=10, ipady=10)

armbk = Button(root, text="ARM BK", bg="blue", command=armbackward)
armbk.pack(side=BOTTOM, padx=10, pady=10, ipadx=10, ipady=10)

clr = Button(root, text="CLEANUP", bg="white", command=clean)
clr.pack(side=LEFT, padx=10, pady=10)

st = Button(root, text="STOP", bg="red", command=stop)
st.pack(side=LEFT, padx=10, pady=10)

button = Button(root, text="Quit", bg="red", command=quit)
button.pack(side=LEFT, padx=10, pady=10)

ledon = Button(root, text="ON", bg="blue", command=ledon)
ledon.pack(side=LEFT, padx=10, pady=10)
ledoff = Button(root, text="OFF", bg="blue", command=ledoff)
ledoff.pack(side=LEFT, padx=10, pady=10)

armst = Button(root, text="STOP ARM", bg="red", command=armstop)
armst.pack(side=TOP, padx=10, pady=10)

gripst = Button(root, text="STOP GRIP", bg="red", command=gripstop)
gripst.pack(side=TOP, padx=10, pady=10)

root.title("Motor GUI")
root.geometry('500x300+200+200')

root.mainloop()
