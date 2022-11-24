from datetime import date


class Ticket():
    def __init__(self, userData):
        self.userData = userData

    def getTicket(self):
        name = self.userData.surname.split(" ")
        childTicket = self.userData.children > 0 and f"Child ticket:       {self.userData.children}         £{12*self.userData.children}.00" or ""
        adultTicket = self.userData.adults > 0 and f"\n        Adult ticket:       {self.userData.adults}         £{20*self.userData.adults}.00" or ""
        seniorTicket = self.userData.seniors > 0 and f"\n        Senior ticket:      {self.userData.seniors}         £{11*self.userData.seniors}.00" or ""
        bands = self.userData.bands > 0 and f"\n        Wristbands:        {self.userData.bands}          £{20*self.userData.bands}.00" or ""

        ticket = f"""
        Copington Theme Park

        Date: {date.today().strftime("%d/%m/%y")}
        Item#             QTY       PRICE
        --------------------------------------
        {childTicket}{adultTicket}{seniorTicket}{bands}
        --------------------------------------
                              SUBTOTAL: £{self.userData.calculateCost()}.00
                              AMOUNT PAYED £{self.userData.amountPayed()}.00
                              CHANGE: £{max(self.userData.amountPayed()-self.userData.calculateCost(), 0)}.00
            LEAD BOOKER: {self.userData.surname.upper()}

        """
        return ticket
