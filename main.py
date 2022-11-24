from time import sleep
from user_data import UserData
from ticket import Ticket
from park_data import ParkData
from parking_pass import ParkingPass

PARKDATA = ParkData(12, 20, 11, 20, 0, 500)


def getDataToChange():
    dataToChange = ""
    allData = [data+", " for data in PARKDATA.getIterableData()]
    allData[len(allData)-1] = allData[len(allData)-1].split(",")[0]
    while dataToChange not in allData and dataToChange+", " not in allData:
        dataToChange = input(
            f"Which data would you like to change ({''.join(allData)})? ").strip()
        if dataToChange not in allData and dataToChange+", " not in allData:
            print(f"You must enter {''.join(allData)}.")
    return dataToChange


def formatIterableData(iterableData: dict):
    returnData = ""
    for data in iterableData:
        returnData += f"{data}: {iterableData[data]}\n      "
    return returnData


def admin():
    print("Welcome to the admin panel")
    inAdmin = True
    while inAdmin:
        currentData = PARKDATA.getIterableData()
        print(
            f"Current park data: \n    {formatIterableData(currentData)}")
        PARKDATA.changeData(getDataToChange(), getInt(
            "What would you like to change the value to? "))
        inAdmin = yesOrNo("Would you like to stay in admin mode (y or n)? ")


def getName():
    name = None
    while not name:
        name = input("What is your name: ")
        if name.strip() == "":
            name = None
            print("You must enter a name.")
        elif name == "rootADMIN":
            admin()
    return name


def getInt(message):
    valid = False
    while not valid:
        integer = input(message)
        try:
            integer = int(integer)
            if integer < 0:
                int("fred")  # raises a ValueError
            valid = True
        except ValueError:
            print("You must enter a whole number greater than 0")
    return integer


def yesOrNo(message):
    valid = False
    while not valid:
        yesOrNo = input(message).lower()
        valid = (yesOrNo == "y" or yesOrNo == "n")
    return yesOrNo == "y"


def pay(userData):
    while userData.change() < 0:
        print(f"The cost is £{userData.calculateCost()}.00")
        userData.setNotes("notes20", 0)
        userData.setNotes("notes10", 0)
        userData.setNotes("notes20", getInt("How many £20 will you use? "))
        if userData.change() < 0:
            print(f"The remaining cost is £{userData.change()*-1}.00")
            userData.setNotes("notes10", getInt("How many £10 will you use? "))
        if userData.change() < 0:
            print("You must cover the full cost.")


def tooManyPeople(children, adults, seniors):
    return children + adults + seniors > PARKDATA.maxPersonsInPark


def main():
    while True:
        print("Welcome to Copington Theme Park")
        splitName = getName().split(" ")
        surname = splitName[len(splitName)-1]
        children = getInt(
            f"How many children are there? (£{PARKDATA.childCost} each): ")
        adults = getInt(
            f"How many adults are there? (£{PARKDATA.adultCost} each): ")
        seniors = getInt(
            f"How many seniors are there? (£{PARKDATA.seniorCost} each): ")
        bands = getInt(
            f"How many wristbands do you want? (£{PARKDATA.wristbandCost} each): ")
        if tooManyPeople(children, adults, seniors):
            print("Sorry we are at capacity right now.\nPlease try again later.")
        else:
            parking = yesOrNo("Do you need a parking pass (y or n): ")
            userData = UserData(children, adults, seniors,
                                bands, parking, surname)
            pay(userData)
            ticket = Ticket(userData)
            print(ticket.getTicket())
            if userData.parking:
                print(ParkingPass(surname).getPass())
            print("Thank you for coming to Copington Theme Park")

        sleep(2)


if __name__ == "__main__":
    main()
else:
    raise("You cannot import this program as a module.")
