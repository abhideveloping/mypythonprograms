#program to get the factorial of a number given by the user.
class fact:
    def check(self):
        a = int(input("Please enter the number: "))
        result = a - 1
        while result !=0:
            a = a*result
            result=result - 1
        print(a)
        
fo = fact()
fo.check()