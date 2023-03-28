class Garage():
    def __init__(self,capacity,cars):
        self.capacity = capacity
        self.cars = cars
    
    def showCars(self):
        print("Here are all of the cars in the garage: ")
        for i in self.cars:
            print(i)

    def addCar(self):
        carIn = input("What is your lisence plate number?: ")
        self.cars.append(carIn)

    def removeCar(self):
        carOut = input("What is your lisence plate number?: ")
        self.cars.remove(carOut)
        print("Thank you, have a nice day")

myGarage = Garage(20,[])

def run():
    while True:
        tickets = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        parking_spaces = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
        currentTicket = {}

        response = input("Are you entering? or Leaving? : ")
        if response.lower() == "leaving":
            hours = input("How many hours were you here rounded to nearest hour?: ")
            cost = int(hours)* 5
            stCost = str(cost)
            costIn = input("Your total cost is $"+ stCost + " please enter that amount now: ")
            if costIn == stCost:
                myGarage.removeCar()
                tickets.append(currentTicket[0])
                
            else:
                print("please enter $"+ stCost + " as a whole integer: ")
            
        elif response.lower() == "show":
            myGarage.showCars()
                
        else:
            myGarage.addCar()
            print("Here is your ticket, please keep track of the time that you are parked here. ")
            currentTicket.append(tickets[0])
            
                    


run()
