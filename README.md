About the program:
I created this program because I wanted to be able to insert characters without changing keyboard layouts, using hotkeys, or opening a word processor window and finding the character I want in the sea of characters I don't care about.

This program allows the user to type in a text field and use the displayed keyboard to insert special characters as they want without breaking concentration. 

This program uses utf-8 character codes for characters that aren't on a standard keyboard, because python is picky about what kinds of characters are in its files.

The characters I programmed into the program are those that I need, or those that seem logical to include given other characters (why only have three characters of the Greek alphabet?). Suggestions are welcome, but if you suggest letters or a new letterset, please also include the utf-8 character code for the letter, or the range that the codes can be found in. Or, if you're feeling ambitious, add the letters to the letters file and a corresponding reference in keyboard.py and submit a pull request.

To run this program, run keyboard.py; it uses the other files. This program requires the Tkinter library to run. Hit escape or press the shift button to toggle in-program shift (well, caps lock).


