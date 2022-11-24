class UserData():
    def __init__(self, children=0, adults=0, seniors=0, bands=0, parking=False, surname="", notes10=0, notes20=0):
        self.children = children
        self.adults = adults 
        self.seniors = seniors 
        self.bands = bands
        self.parking = parking
        self.surname = surname
        self.notes10 = notes10
        self.notes20 = notes20

    def setNotes(self, type:str, amount:int):
        if type == "notes10":
            self.notes10 = amount
        elif type == "notes20":
            self.notes20 = amount
        else:
            raise("Invalid type submitted.")

    def calculateCost(self):
        return (self.children * 12) + (self.seniors * 11) + (self.adults * 20) + (self.bands * 20)

    def amountPayed(self):
        return self.notes10 * 10 + self.notes20 * 20

    def change(self):
        return self.amountPayed() - self.calculateCost()