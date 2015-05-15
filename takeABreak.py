__author__ = 'user'


import webbrowser
import time

print("The Program Started By " + time.ctime())
total_break = 0;
while(total_break <= 3) :
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=5ts5QWTBR-w")
    total_break = total_break + 1
