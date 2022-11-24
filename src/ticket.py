from datetime import date
class Ticket():
    def __init__(self, userData):
        self.userData = userData

    def getTicket(self):
        name = self.userData.name.split(" ")
        childTicket = self.userData.children > 0 and f"Child ticket:       {self.userData.children}         £{12*self.userData.children}.00"
        adultTicket = self.userData.adult > 0 and f"Adult ticket:       {self.userData.adults}         £{20*self.userData.adults}.00"
        seniorTicket = self.userData.children > 0 and f"Senior ticket:       {self.userData.seniors}         £{11*self.userData.seniors}.00"
        
        ticket = f"""
        Copington Theme Park

        Date: {date.today()}
        Item#             QTY       PRICE
        --------------------------------------
        {childTicket}
        {adultTicket}
        {seniorTicket}
        --------------------------------------
                              SUBTOTAL: £{self.userData.calculateCost()}.00
                              CHANGE: £{max(self.userData.amountPayed()-self.userData.calculateCost(), 0)}.00
        """
        return ticket
