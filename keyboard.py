from Tkinter import *
import Tkinter as tk
import time
from letters import *
import sys

#I don't think I'll be needing this unless I can program this not to count
#itself as a window or send keystrokes to the second window on the alt-tab stack

#import subprocess

shiftDown = True
alphabet = "greek"
kbd = [] #this will be a two-dimensional array of keys
#I will also need a shift key, maybe detect if shift is used on hw. kbd?
letters = {} #this will hold a hash table of letters

def toggleShift(var=None):
    global shiftDown
    if shiftDown:
        shiftDown = False
        shift.config(bg = "#EEE", text = u'\u2191 Shift \u2191')
    else:
        shiftDown = True
        shift.config(bg = "#AAA", text = u'\u2193 Shift \u2193')
    change(alphabet)
    
def typeLetter(letter):
    myLetter = 'a'
    if shiftDown:
        myLetter = letter[0]
    else:
        myLetter = letter[1]
    print output.get('0.0', END).strip('\n') + myLetter
    sys.stdout.flush()
    output.insert(INSERT, myLetter)
    output.focus_set()

def clearToPoint(point=END, begin='0.0'):
    output.delete(begin, point)

def change(newAlphabet):
    global alphabet
    alphabet = newAlphabet
    global kbd
    if len(kbd) > 0:
        for i in kbd:
            i.pack_forget()

    letters = {}
    letterset = []
    caps = {}
    lower = {}
    kbd = []
    if newAlphabet == "greek":
        letterset = greekLetters
        caps = greekCLetters
        lower = greekLLetters

    elif newAlphabet == "english":
        letterset = englishLetters
        caps = englishCLetters
        lower = englishLLetters

    elif newAlphabet == "symbols":
        letterset = symbols
        caps = symbolLetters
        lower = symbolLetters

    elif newAlphabet == "circles":
        letterset = circles
        caps = circledCLetters
        lower = circledLLetters
        
    for i in letterset:
        #give keys both upper and lower, and toggle if [0] or [1] is
        #displayed/used by using shift
        letters[i] = [caps[i], lower[i]]


    
    height = 3
    width = (len(letters) / height) + 1
    if alphabet == "english" or newAlphabet == "circles":
        width = 10
        height = len(letters) / 10 + 1
    elif alphabet == "symbols":
        width = 11
        height = len(letters) / 11 + 1
    rows = 0
    count = 0
#    f = Frame(keyboardFrame)
#    kbd.append(f.pack(side=TOP))
#    print f, kbd
    buttons = []
    for i in range(height):
        kbd.append(Frame(keyboardFrame))
        kbd[i].pack(side=TOP)
    for letter in letterset:
        if count == width:
            count = 0
            rows += 1
        if shiftDown:
            myText = letters[letter][0]
        else:
            myText = letters[letter][1]
        myCommand =  lambda letter = letter: typeLetter(letters[letter])
        b = Button(kbd[rows], text = myText, command = myCommand)
        b.pack(side=LEFT)
        count += 1




root = Tk()
root.title("UTF-8 Keyboard")
icon = PhotoImage(file="joystick.png")
root.tk.call('wm', 'iconphoto', root._w, icon)

leftFrame = Frame(root)
keyboardFrame = Frame(leftFrame)
selectionFrame = Frame(root)
textFrame = Frame(leftFrame)
output = Text(textFrame, height = 3, width = 70)

shift = Button(selectionFrame, text = u'\u2193 Shift \u2193', command = lambda: toggleShift())

greekButton = Button(selectionFrame, text = "Greek", command = lambda: change("greek"))
englishButton = Button(selectionFrame, text = "English", command = lambda: change("english"))
symbolButton = Button(selectionFrame, text = "Symbols", command = lambda: change("symbols"))
circlesButton = Button(selectionFrame, text = "Circles", command = lambda: change("circles"))
clear = Button(selectionFrame, text = "Clear", command = lambda: clearToPoint())

leftFrame.pack(side=LEFT)
keyboardFrame.pack(side=TOP, fill=BOTH)
keyboardFrame.config(bg = "#3C3B37")
selectionFrame.pack(side=RIGHT)
textFrame.pack(side=BOTTOM)
output.pack()

shift.pack()
shift.config(bg = "#AAA")
greekButton.pack(side=TOP)
greekButton.focus_set()
symbolButton.pack(side=TOP)
circlesButton.pack(side=TOP)
englishButton.pack(side=TOP)
clear.pack(side=TOP)


change("greek")

root.bind("<Escape>", toggleShift)
#root.bind("<Control-u>", lambda x: clearToPoint(INSERT, "linestart"))
root.bind("<Control-u>", lambda x: clearToPoint(INSERT, output.index(INSERT)[0]+'.0'))


root.mainloop()




#I'll also need a text entry area for the char's
