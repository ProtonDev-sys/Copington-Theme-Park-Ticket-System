import tkinter as tk
from utils import makeAdder, getRelativeY
from ticket import Ticket
HEIGHT = 400
WIDTH = 300
TITLE = "Copington Adventure Theme Park"
OFFSET = 0.07

class UserInterface():
    def __init__(self, userData):
        self.userData = userData
        
        self.window = tk.Tk() # Make and setup the window
        self.window.title(TITLE)
        self.window.geometry(f"{WIDTH}x{HEIGHT}")

        self.defineData() # stores all the data we need from userData
        self.makeWidgets() # puts widgets on the screen
        self.window.mainloop() # keeps the screen open

    def defineData(self):
        self.notes10 = tk.StringVar()
        self.notes10.set("0")

        self.notes20 = tk.StringVar()
        self.notes20.set("0")
        

    def makeWidgets(self):
        tk.Label(self.window, text="Enter your cash now").place(relx=.5, rely=0.04, anchor="center")
        makeAdder(self.window, "£10 notes", self.remove10Note, self.add10Note, 4, self.notes10, OFFSET)
        makeAdder(self.window, "£20 notes", self.remove20Note, self.add20Note, 5, self.notes20, OFFSET)

        self.amountPayed = tk.StringVar()
        self.amountPayed.set(f"Amount payed: £{self.userData.amountPayed()}.00")
        self.change = tk.StringVar()
        self.change.set(f"Change: £{max(self.userData.amountPayed()-self.userData.calculateCost(), 0)}.00")

        tk.Label(self.window, text=f"Amount to pay: £{self.userData.calculateCost()}.00").place(relx=0.2, rely=getRelativeY(7, OFFSET), anchor="center")
        tk.Label(self.window, textvariable=self.amountPayed).place(relx=0.2, rely=getRelativeY(8, OFFSET), anchor="center")
        tk.Label(self.window, textvariable=self.change).place(relx=0.15, rely=getRelativeY(9, OFFSET), anchor="center")
        tk.Button(self.window, text="Pay", command=self.pay).place(relx=0.5, rely=getRelativeY(11, OFFSET), anchor="center")
        
    def updateTextVariables(self):
        self.amountPayed.set(f"Amount payed: £{self.userData.amountPayed()}.00")
        self.change.set(f"Change: £{max(self.userData.amountPayed()-self.userData.calculateCost(), 0)}.00")
    
    def add10Note(self):
        self.userData.add10Note()
        self.notes10.set(self.userData.notes10)
        self.updateTextVariables()

    def remove10Note(self):
        self.userData.remove10Note()
        self.notes10.set(self.userData.notes10)
        self.updateTextVariables()

    def add20Note(self):
        self.userData.add20Note()
        self.notes20.set(self.userData.notes20)
        self.updateTextVariables()

    def remove20Note(self):
        self.userData.remove20Note()
        self.notes20.set(self.userData.notes20)
        self.updateTextVariables()

    def pay(self):
        print(Ticket(self.userData).getTicket())