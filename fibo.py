class figo:
    def work(self):
        a = int(input("enter the number of terms for fibonacci series: "))
        
        b=0;
        c=1;
        d=0;
        print(b)
        print(c)
        for i in range(0, a-2):
            d = b+c
            print(d)
            b = c
            c = d
fo = figo()
fo.work()
            