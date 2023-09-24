class age:
    def work(self):
        a = int(input("Kindly enter you age to check: "))
        
        if a >18:
            print("you can't drive since your age are underage")
        
        elif a<=18:
            print("you can drive you are an adult")
            

ao = age()
ao.work()