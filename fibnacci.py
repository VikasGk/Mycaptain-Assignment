n=int(input("enters nubers you want to print in fib nacci series"))

a=0
b=1
c=0
i=0

if n<=0:
    print("enter a positive number")
elif n==1:
    print(a)
else:
    while i<n:
        if i==0:
            print(a)
        elif i==1:
             print(b)
        else:
              c=a+b
              print(c)
              a,b=b,c
        i=i+1     
        
        
