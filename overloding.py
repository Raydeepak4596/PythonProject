class Bike:
    def __init__(self,bikenumber):
        self.bikenumber=bikenumber
    def showtotalbike(self):
        print("Total number of bike in stock for Rental : " +str(self. bikenumber))
    def rentbike(self,rent):
        self.rent=rent
        print("Total coast of bike for rent : "+ str(self.rent * 100))
        print("Total coast of bike for rent : "+str( self.bikenumber - self.rent))
    
obj=Bike(100)
intt=int(input("How many bike do you rent : "))
obj.showtotalbike()
obj.rentbike(intt)