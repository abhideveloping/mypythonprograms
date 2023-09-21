class calculator:
    def calc(self):
        print("1.Addition")
        print("2.Substraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")
        a = int(input("Please enter the operation 1/2/3/4/5: "))
        b = float(input("Enter the first number:  "))
        c = float(input("Enter the second number:  "))
        
        if a == 1:
            result = b+c
            print(result)
        
        elif a == 2:
            result = b - c
            print(result) 
            
        elif a == 3:
            result = b*c 
            print(result)
        
        elif a == 4:
            result = b/c
            print(result)
        
ca = calculator()
ca.calc()   
        
    
    
        