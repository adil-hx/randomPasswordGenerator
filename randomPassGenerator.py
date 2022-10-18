from tkinter import *
from tkinter import ttk
import pyperclip
import random 

GUI = Tk()
GUI.geometry("400x400")

passwordString = StringVar()
passwordLength = IntVar()
passwordLength.set(0)

def generatePassword():
    password1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', '*' ',', '(,)']
    password = ""
    for x in range(passwordLength.get()):
        password = password + random.choice(password1)
    passwordString.set(password)

def copyToClipboard():
    randomPassword = passwordString.get()
    pyperclip.copy(randomPassword)
    Label(GUI,text="Copied password to clipboard", font="calibiri 5")

Label(GUI, text = "Passsword Generator", font= "calibri 20 bold").pack()
Label(GUI, text="Enter Password Length").pack(pady=3)
Entry(GUI, textvariable=passwordLength).pack(pady=3)
Button(GUI,text="Generate Password", command=generatePassword).pack(pady=7)
Entry(GUI,textvariable=passwordString).pack(pady=3)
Button(GUI, text="Copy to clipboard", command=copyToClipboard).pack()

GUI.resizable(False,False)
GUI.title("Random Password Generator")
mainloop()

