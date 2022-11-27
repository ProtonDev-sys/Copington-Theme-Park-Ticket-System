class UserData():
    def __init__(self: UserData, children=0, adults=0, seniors=0, bands=0, parking=False, surname="", notes10=0, notes20=0) -> None:
        self.children = children
        self.adults = adults
        self.seniors = seniors
        self.bands = bands
        self.parking = parking
        self.surname = surname
        self.notes10 = notes10
        self.notes20 = notes20

    def setNotes(self: UserData, type: str, amount: int) -> None:
        if type == "notes10":
            self.notes10 = amount
        elif type == "notes20":
            self.notes20 = amount
        else:
            raise("Invalid type submitted.")

    def calculateCost(self: UserData) -> int:
        return (self.children * 12) + (self.seniors * 11) + (self.adults * 20) + (self.bands * 20)

    def amountPayed(self: UserData) -> int:
        return self.notes10 * 10 + self.notes20 * 20

    def change(self: UserData) -> int:
        return self.amountPayed() - self.calculateCost()
