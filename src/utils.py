import tkinter as tk 

def makeAdder(window, label, removeCommand, addCommand, row, textVariable, offset):
    relativeY = getRelativeY(row, offset)
    tk.Label(window, text=label).place(relx=0.1, rely=relativeY, anchor="center")
    tk.Button(window, height=1, width=1, text="-", command=removeCommand).place(relx=0.25, rely=relativeY, anchor="center")
    tk.Label(window, textvariable=textVariable, width=1).place(relx=0.3, rely=relativeY, anchor="center")
    tk.Button(window, height=1, width=1, text="+", command=addCommand).place(relx=0.35, rely=relativeY, anchor="center")

def getRelativeY(row, offset):
    relativeY = (row*offset) - offset
    return relativeY