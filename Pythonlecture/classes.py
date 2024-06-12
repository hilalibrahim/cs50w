# class point():
#     def __init__(self,input1,input2):
#         self.x=input1
#         self.y=input2
# p=point(2,3)
# print(p.x)
# print(p.y)
class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passenger=[]
    def add_passenger(self,name):
        if not self.open_seats():
            return False
        self.passenger.append(name)
        return True
    def open_seats(self):
        return self.capacity-len(self.passenger)
flight=Flight(3)
people=["Harry","Ron","Hermione","Ginny"]
for person in people:
   success=flight.add_passenger(person)
   if success:
    print(f"Added {person} to the flight successfully")
   else:
      print(f"No available seats for {person}")
       
   

