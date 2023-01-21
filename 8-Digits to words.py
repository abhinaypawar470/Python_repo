num=int(input("Enter the Number:-"))
n=num
rnum=0
i=0
a=[0,0,0,0,0,0,0,0,0,0]

while(n!=0):
    rem=n%10
    a[i]=rnum*10+rem
    n=n//10
    i=i+1
