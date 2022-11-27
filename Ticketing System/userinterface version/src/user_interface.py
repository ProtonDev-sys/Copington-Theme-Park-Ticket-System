import tkinter as tk

class UserInterface():
    def __init__(self, userData):
        self.userData = userData
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
        self.window = tk.Tk()
        self.window.title("Copington Adventure Theme Park")
        self.window.geometry("500x300")

        self.makeWidgets()
        self.window.mainloop()

    def makeWidgets(self):
        heading = tk.Label(self.window, text="Welcome to Copington Adventure Theme Park").grid(row=0, column=5)
        name = tk.Label(self.window, text="Name:").grid(row=3,column=1)
        nameField = tk.Text(self.window, height=1, width=20).grid(row=3, column=2)

        self.makeAdder(self.window, "Children", self.removeChild, self.addChild, 4, self.children)
        self.makeAdder(self.window, "Adults", self.removeAdult, self.addAdult, 5, self.adults)
        self.makeAdder(self.window, "Seniors", self.removeSenior, self.addSenior, 6, self.seniors)
        self.makeAdder(self.window, "Wristbands", self.removePass, self.addPass, 7, self.passes)

        tk.Label(self.window, text="Parking").grid(row=8, column=1)
        tk.Button(self.window, textvariable=self.parking, command=self.changeParking).grid(row=8,column=2)

        tk.Label(self.window, textvariable=self.cost).grid(row=9,column=3)
        tk.Button(self.window, text="Submit", command=self.submit).grid(row=10,column=3)
        tk.Label(self.window, textvariable=self.issueText).grid(row=11,column=3)

    def makeAdder(self, window, label, removeCommand, addCommand, row, textVariable):
        tk.Label(window, text=label).grid(row=row, column=1)
        tk.Button(window, height=1, width=1, text="-", command=removeCommand).grid(row=row, column=2)
        tk.Label(window, textvariable=textVariable, width=1).grid(row=row, column=3)
        tk.Button(window, height=1, width=1, text="+", command=addCommand).grid(row=row, column=4)

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

    def submit(self):
        if self.userData.calculateCost() == 0:
            self.issue("You must buy something")
        elif self.userData.passes > (self.userData.children + self.userData.adults + self.userData.seniors):
            self.issue("You cannot buy more wristbands than tere are people")
