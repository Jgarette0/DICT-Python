class Customers: 
 greeting = "Welcome to the Coffee Palace!"
 
 def __init__(self,name):
  self.name = name
  
samirah = Customers("Samirah ")
jerry = Customers("Jerry ")
samirah.bevarage = "Cinnamon Roll"


print(samirah.name + samirah.greeting)
print(Customers.greeting)
print(samirah.bevarage)
# greeting = "Welcome to the Coffee Palace!"
# name = Samirah , Jerry
# bevarage = Ice Cafe Latte, Caramel Macchiato
# food =  Cinnamon Roll, Glazed Doughnut
# Total = 225,230