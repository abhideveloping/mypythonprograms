# a python program just to check the name of the dog.
class Animal:
    # attribute and method of the parent class
    name = "Tommy"
     
    def eat(self):
        print("I can eat")
        
        
class Dog(Animal):
    def display(self):
        print("my name is ", self.name)
        
#create an object of the subclass

labrador = Dog()

# Access superclass attribute and method


#call subclass method

labrador.display()
         