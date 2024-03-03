class Dog:
 def __init__(self, name):
  self.name = name
  
 def bark(self):
  print(f"{self.name} is barking")  

husky = Dog("Cloudnine")
husky.bark()

class Person:
 def __init__(self,firstname,lastname):
  self.firstname = firstname
  self.lastname = lastname
  
nigga = Person("Niga", "What")

print(nigga.firstname +" "+ nigga.lastname)


# Dog class
class Dog:
    # bark method
    def __init__(self, name):
        # initialize with name
        self.name = name

    # make dog bark
    def bark(self):
        print(f"{self.name} is barking")

# create Dog instance
husky = Dog("Cloudnine")
# make husky bark
husky.bark()

