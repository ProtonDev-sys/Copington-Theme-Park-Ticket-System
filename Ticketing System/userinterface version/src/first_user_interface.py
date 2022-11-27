import tkinter as tk
from payment_user_interface import UserInterface as paymentUI
from utils import makeAdder, getRelativeY

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
        self.adults = tk.StringVar()
        self.adults.set(self.userData.adults)

        self.children = tk.StringVar()
        self.children.set(self.userData.children)

        self.seniors = tk.StringVar() 
        self.seniors.set(self.userData.seniors)

        self.passes = tk.StringVar()
        self.passes.set(self.userData.passes)

        self.parking = tk.StringVar()
        self.parking.set((self.userData.passes and "Yes" or "No"))

        self.cost = tk.StringVar()
        self.cost.set(f"Subtotal: £{self.userData.calculateCost()}.00")

        self.issueText = tk.StringVar()

    def makeWidgets(self):
        heading = tk.Label(self.window, text="Welcome to Copington Adventure Theme Park").place(relx=.5, rely=0.04, anchor="center")
        
        name = tk.Label(self.window, text="Name:").place(relx=0.1, rely=0.1, anchor="center")
        self.nameField = tk.Text(self.window, height=1, width=20)
        self.nameField.place(relx=0.5, rely=0.1, anchor="center")
    
        makeAdder(self.window, "Children", self.removeChild, self.addChild, 4, self.children, OFFSET)
        makeAdder(self.window, "Adults", self.removeAdult, self.addAdult, 5, self.adults, OFFSET)
        makeAdder(self.window, "Seniors", self.removeSenior, self.addSenior, 6, self.seniors, OFFSET)
        makeAdder(self.window, "Wristbands", self.removePass, self.addPass, 7, self.passes, OFFSET)
        
        tk.Label(self.window, text="Parking").place(relx=0.1, rely=getRelativeY(8, OFFSET), anchor="center")
        tk.Button(self.window, textvariable=self.parking, command=self.changeParking).place(relx=0.3, rely=getRelativeY(8, OFFSET), anchor="center")

        tk.Label(self.window, textvariable=self.cost).place(relx=0.5, rely=getRelativeY(9, OFFSET), anchor="center")
        tk.Button(self.window, text="Pay", command=self.submit).place(relx=0.5, rely=getRelativeY(10, OFFSET), anchor="center")
        tk.Label(self.window, textvariable=self.issueText).place(relx=0.5, rely=getRelativeY(11, OFFSET), anchor="center")

    def updateCost(self):
        self.cost.set(f"Subtotal: £{self.userData.calculateCost()}.00")

    def addAdult(self):
        self.userData.addAdult()
        self.adults.set(str(self.userData.adults))
        self.updateCost()

    def removeAdult(self):
        self.userData.removeAdult()
        self.adults.set(str(self.userData.adults))
        self.updateCost()

    def addChild(self):
        self.userData.addChild()
        self.children.set(str(self.userData.children))
        self.updateCost()

    def removeChild(self):
        self.userData.removeChild()
        self.children.set(str(self.userData.children))
        self.updateCost()

    def addSenior(self):
        self.userData.addSenior()
        self.seniors.set(str(self.userData.seniors))
        self.updateCost()

    def removeSenior(self):
        self.userData.removeSenior()
        self.seniors.set(str(self.userData.seniors))
        self.updateCost()

    def addPass(self):
        self.userData.addPass()
        self.passes.set(str(self.userData.passes))
        self.updateCost()

    def removePass(self):
        self.userData.removePass()
        self.passes.set(str(self.userData.passes))
        self.updateCost()

    def changeParking(self):
        self.userData.changeParking()
        self.parking.set((self.userData.parking and "Yes" or "No"))

    def issue(self, text):
        self.issueText.set(text)

    def updateName(self):
        self.name = self.nameField.get(1.0, "end-1c")
        self.userData.setName(self.name)

    def submit(self):
        self.updateName() 
        if self.userData.calculateCost() == 0:
            self.issue("You must buy something.")
        elif self.userData.passes > (self.userData.children + self.userData.adults + self.userData.seniors):
            self.issue("You cannot buy more wristbands than there are people.")
        elif self.userData.name.strip() == "":
            self.issue("You must input a name.")
        else:
            self.window.destroy()
            paymentUI(self.userData)
