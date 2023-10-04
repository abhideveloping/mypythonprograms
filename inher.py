# python program just to check and see how inheritance work
class Animal:
    # Attribute and method of the parent class
    name = ""
    
    def eat(self):
        print("i can eat")

    #inherit from animal
class Dog(Animal):
    #override eat() method 
    def eat(self):
        print('I like to eat bones')
        
#create an object of the subclass
larbador = Dog()
larbador.eat()
    