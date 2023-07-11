class Train:

    seat=[]

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.seat=[None]*seats
    def getStatus(self):
        print("************")
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")
        print(self.seat)
        print("************")

    def fareInfo(self):
        print(f"The price of the ticket is: Rs {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
            self.seat[self.seats]="Booked"
        else:
            print("Sorry this train is full! Kindly try in tatkal")

    def cancelTicket(self, seatNo):
        # seat=[None]*self.seats
        self.seat[seatNo]="None"
        self.seats+=1


intercity = Train("Intercity Express: 14015", 90, 2)
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.bookTicket()
intercity.getStatus()
intercity.cancelTicket(1)
intercity.getStatus()

