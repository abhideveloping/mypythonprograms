class table:
     def calc(self):
         a = int(input("Enter the number you want table for: "))
         for i in range(1, 11):
             result = a*i;
             print(result)

to = table()
to.calc()