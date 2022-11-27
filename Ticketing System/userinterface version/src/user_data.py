class UserData():
    def __init__(self, children=0, adults=0, seniors=0, passes=0, parking=False, name=""):
        self.children = children
        self.adults = adults 
        self.seniors = seniors 
        self.passes = passes
        self.parking = parking
        self.name = name
        self.notes10 = 0
        self.notes20 = 0

    def addChild(self):
        self.children += 1 

    def removeChild(self):
        if (self.children > 0):
            self.children -= 1

    def setChildren(self, amount:int):
        self.children = amount

    def addAdult(self):
        self.adults += 1

    def removeAdult(self):
        if (self.adults > 0):
            self.adults -= 1

    def setAdults(self, amount:int):
        self.adults = amount 

    def addSenior(self):
        self.seniors += 1

    def removeSenior(self):
        if (self.seniors > 0):
            self.seniors -= 1
    
    def setSeniors(self, amount:int):
        self.seniors = amount 

    def addPass(self):
        self.passes += 1

    def removePass(self):
        if (self.passes > 0):
            self.passes -= 1

    def setPasses(self, amount:int):
        self.passes -= 1

    def changeParking(self):
        self.parking = not self.parking

    def setParking(self, value:bool):
        self.parking = value

    def setName(self, name:str):
        self.name = name

    def calculateCost(self):
        return (self.children * 12) + (self.seniors * 11) + (self.adults * 20) + (self.passes * 20)

    def add10Note(self):
        self.notes10 += 1

    def remove10Note(self):
        if self.notes10 > 0:
            self.notes10 -= 1

    def add20Note(self):
        self.notes20 += 1
    
    def remove20Note(self):
        if self.notes20 > 0:
            self.notes20 -= 1

    def amountPayed(self):
        return self.notes10 * 10 + self.notes20 * 20