import datetime


class ParkingPass():
    def __init__(self: ParkingPass, name: str) -> None:
        self.name = name

    def getPass(self: ParkingPass) -> str:
        time = datetime.datetime.now()
        return f"""
        TEMPORARY PARKING PASS FOR 
                  {self.name}
            ACTIVE FROM {time.day}/{time.month} {time.hour}:{time.minute}
                    FOR 12 HOURS
        """
