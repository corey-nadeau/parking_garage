class Garage():
    def __init__(self):
        self.tickets = 20
        self.spaces = 20
        self.currentTicket = {'owed':[], 'paid':[]}
        self.dailyProfit = []

    def addCar(self):
        if self.spaces < 1:
            print('Garage full. Please come back another time.')
        carIn = input("What is your lisence plate number?: ")
        id = carIn.lower()
        self.currentTicket['owed'].append(id)
        self.tickets = self.tickets -1
        self.spaces = self.spaces -1
        print(f'Please proceed to nearest available space. ({self.tickets} spaces remaining.)')

    def removeCar(self):
        carOut = input("What is your lisence plate number?: ")
        idOut = carOut.lower()
        if idOut in self.currentTicket['owed']:
            hours = input("How many hours were you here rounded to nearest hour?: ")
            cost = int(hours)* 5
            stCost = str(cost)
            costIn = input("Your total cost is $"+ stCost + " please enter that amount now: ")
            if costIn == stCost:
                self.dailyProfit.append(costIn)
                self.currentTicket['owed'].remove(idOut)
                self.currentTicket['paid'].append(idOut)
                self.tickets - self.tickets + 1
                self.spaces = self.spaces + 1
                print('Thank you, you have 15 minutes to leave. Have a nice day!')
            else: 
                print("please enter $"+ stCost + " as a whole integer: ")   
        elif idOut not in self.currentTicket['owed']:
            print('License plate number not found. Please try again. ')            

myGarage = Garage()

def run():
    while True:

        response = input("Are you Entering? or Leaving? : ")
        if response.lower() == "leaving":
            myGarage.removeCar()
        elif response.lower() == "entering":
            myGarage.addCar()
        
#  admin input only
        elif response.lower() == "showprofit":
            ints = []
            for i in myGarage.dailyProfit:
                ints.append(int(i))
            print(f'Total amount collected today: ${sum(ints)}')

                    


run()
