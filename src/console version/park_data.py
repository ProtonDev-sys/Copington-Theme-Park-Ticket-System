class ParkData():
    def __init__(self, childCost: int, adultCost: int, seniorCost: int, wristbandCost: int, personsInPark: int, maxPersonsInPark: int):
        self.childCost = childCost
        self.adultCost = adultCost
        self.seniorCost = seniorCost
        self.wristbandCost = wristbandCost
        self.personsInPark = personsInPark
        self.maxPersonsInPark = maxPersonsInPark

    def getIterableData(self):
        return {
            "childCost": self.childCost,
            "adultCost": self.adultCost,
            "seniorCost": self.seniorCost,
            "wristbandCost": self.wristbandCost,
            "personsInPark": self.personsInPark,
            "maxPersonsInPark": self.maxPersonsInPark
        }

    def addPersons(self, amount: int):
        self.personsInPark += amount

    def removePersons(self, amount: int):
        self.personsInPark -= amount

    def changeData(self, dataToChange: str, value: int):
        if dataToChange == "childCost":
            self.childCost = value
        elif dataToChange == "adultCost":
            self.adultCost = value
        elif dataToChange == "seniorCost":
            self.seniorCost = value
        elif dataToChange == "wristbandCost":
            self.wristbandCost = value
        elif dataToChange == "personsInPark":
            self.personsInPark = value
        elif dataToChange == "maxPersonsInPark":
            self.maxPersonsInPark = value
        if "Cost" in dataToChange:
            print(f"{dataToChange} changed to £{value}.00")
        else:
            print(f"{dataToChange} changed to {value}")
