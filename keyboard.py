#This program allows the user to "type" characters that are not on a
#standard keyboard.


#this is a list of import commands. If the user doesn't have Tkinter
#or other libraries installed, it will fail gracefully instead of
#crashing.
imports = [
    "from Tkinter import *",
    "import Tkinter as tk",
    "import time",
    "from letters import *",
    "import sys"
]
#failedPackages will keep a record of the names of the packages that
#failed to import, so that the program can go through the entire list
#of packages that it wants to import. This will allow the program to
#give the user a complete list of packages that they need to install,
#instead of only telling the user one at a time.
failedPackages = ''
for i in imports:
    try:
        exec(i)
    except ImportError as error:
        failedPackages += str(error) + '\n'
#if there were any errors in the imports, tell the users what packages
#didn't import, and exit.
if len(failedPackages) > 0:
    print "Some packages could not be imported:"
    print failedPackages
    exit()


shiftDown = True
alphabet = "greek"
kbd = [] #this will be a two-dimensional array of keys
#I will also need a shift key, maybe detect if shift is used on hw. kbd?
letters = {} #this will hold a hash table of letters


#This toggles whether shift is currently being "held down" according
#to the program. I don't currently know a better way to do this. 
def toggleShift(var=None):
    global shiftDown
    if shiftDown:
        shiftDown = False
        shift.config(bg = "#EEE", text = u'\u2191 Shift \u2191')
    else:
        shiftDown = True
        shift.config(bg = "#AAA", text = u'\u2193 Shift \u2193')
    change(alphabet)

#This inserts a letter at the cursor and prints whatever's in the text
#entry box to the console
def typeLetter(letter):
    print output.get('0.0', END).strip('\n') + letter
    sys.stdout.flush()
    output.insert(INSERT, letter)
    output.focus_set()

#I use ctrl-u a lot, so I programmed it into this program. This
#function is called by hitting ctrl-u.
def clearToPoint(point=END, begin='0.0'):
    output.delete(begin, point)

#This changes the displayed keyboard.
def change(newAlphabet):
    global alphabet
    alphabet = newAlphabet
    global kbd
    if len(kbd) > 0:
        for i in kbd:
            i.pack_forget()

    #letterOrder is an array of the letters, so that I can define the order
    letterOrder = []
    #letterSet is a hash table of the new letters
    letterSet = {}

    letters = {}
    caps = True #whether or not the set of characters has a capitalization
    kbd = []

    #decide which letter table to use
    if newAlphabet == "greek":
        letterOrder = greek
        letters = greekLetters

    elif newAlphabet == "english":
        letterOrder = english
        letters = englishLetters

    elif newAlphabet == "symbols":
        letterOrder = symbols
        letters = symbolLetters

    elif newAlphabet == "circles":
        letterOrder = circles
        letters = circledLetters

    if len(letters[letterOrder[0]]) == 1:
        caps = False
    
    #some specific formatting for certain character sets
    height = 3
    width = (len(letters) / height) + 1
    if alphabet == "english" or newAlphabet == "circles" or newAlphabet == "greek":
        width = 10
        height = len(letters) / 10 + 1
    elif alphabet == "symbols":
        width = 11
        height = len(letters) / 11 + 1
    rows = 0
    count = 0
    buttons = []
    
    #set up the frames
    for i in range(height):
        kbd.append(Frame(keyboardFrame))
        kbd[i].pack(side=TOP)
    #add one more for a space bar
    kbd.append(Frame(keyboardFrame))
    kbd[height].pack(side=TOP)
    
    #make the keyboard
    for letter in letterOrder:
        if count == width:
            count = 0
            rows += 1
        #capital letters are the first entry in the pair
        myLetter = letters[letter][0]
        #this should only put lowercase letters if there are any
        if caps and not shiftDown:
            myLetter = letters[letter][1]
        myCommand =  lambda myLetter = myLetter: typeLetter(myLetter)
        b = Button(kbd[rows], text = myLetter, command = myCommand)
        b.pack(side=LEFT)
        count += 1
    b = Button(kbd[height], text = '[_____________]', command = lambda : typeLetter(' '))
    b.pack()



root = Tk()
root.title("UTF-8 Keyboard")
try:
    icon = PhotoImage(file="icon.png")
    root.tk.call('wm', 'iconphoto', root._w, icon)
except:
    print "Error: could not set icon for this program."

leftFrame = Frame(root)
keyboardFrame = Frame(leftFrame)
selectionFrame = Frame(root)
textFrame = Frame(leftFrame)
output = Text(textFrame, height = 3, width = 70)

shift = Button(selectionFrame, text = u'\u2193 Shift \u2193', command = lambda: toggleShift())

greekButton=Button(selectionFrame,text="Greek",command=lambda:change("greek"))
englishButton=Button(selectionFrame,text="English",command=lambda:change("english"))
symbolButton=Button(selectionFrame,text="Symbols",command=lambda:change("symbols"))
circlesButton=Button(selectionFrame,text="Circles",command=lambda:change("circles"))
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
