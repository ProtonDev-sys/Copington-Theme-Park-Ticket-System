class ParkData():
    def __init__(self: ParkData, childCost: int, adultCost: int, seniorCost: int, wristbandCost: int, personsInPark: int, maxPersonsInPark: int) -> None:
        self.childCost = childCost
        self.adultCost = adultCost
        self.seniorCost = seniorCost
        self.wristbandCost = wristbandCost
        self.personsInPark = personsInPark
        self.maxPersonsInPark = maxPersonsInPark

    def getIterableData(self: ParkData) -> dict:
        return {
            "childCost": self.childCost,
            "adultCost": self.adultCost,
            "seniorCost": self.seniorCost,
            "wristbandCost": self.wristbandCost,
            "personsInPark": self.personsInPark,
            "maxPersonsInPark": self.maxPersonsInPark
        }

    def addPersons(self: ParkData, amount: int) -> None:
        self.personsInPark += amount

    def removePersons(self: ParkData, amount: int) -> None:
        self.personsInPark -= amount

    def changeData(self: ParkData, dataToChange: str, value: int) -> None:
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
