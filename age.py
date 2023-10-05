class age:
    def work(self):
        a = int(input("Kindly enter you age to check: "))
        
        if a >=18:
            print("you are an adult so you can drive")
        
        elif a<=18:
            print("you can't drive since you are underage")
            

ao = age()
ao.work()
