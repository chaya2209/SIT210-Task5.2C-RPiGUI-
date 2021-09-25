from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led=LED(4)
led1=LED(27)
led2=LED(22)

win=Tk()
win.title("LED Toggler")
myfont=tkinter.font.Font(family="Helvetica", size=12, weight="bold")
def ledToggle():
    if led.is_lit:
        led.off()
        ledButton["text"]="Turn led On"
    else:
        led.on()
        ledButton["text"]="Turn led off"
def ledToggle1():
    if led1.is_lit:
        led1.off()
        ledButton1["text"]="Turn led On"
    else:
        led1.on()
        ledButton1["text"]="Turn led off"
        
def ledToggle2():
    if led2.is_lit:
        led2.off()
        ledButton2["text"]="Turn led On"
    else:
        led2.on()
        ledButton2["text"]="Turn led off"
        
ledButton=Button(win,text="Turn led On 4", font=myfont, command=ledToggle, bg='bisque2', height=1, width=24)
ledButton.grid(row=0,column=1)
ledButton1=Button(win,text="Turn led On 27", font=myfont, command=ledToggle1, bg='bisque2', height=1, width=24)
ledButton1.grid(row=1,column=1)
ledButton2=Button(win,text="Turn led On 22", font=myfont, command=ledToggle2, bg='bisque2', height=1, width=24)
ledButton2.grid(row=2,column=1)
                  