#Armstrong number Check
num=int(input("Enter the Number:-"))
n=num
arm=0
power=len(str(num))

while n>0:
    digit=n%10
    arm=arm+digit**power
    n=n//10
    
if num==arm:
    print(num==arm,", It is a Armstrong Number!!!!")
else:
    print(num==arm,", It is not a Armstrong Number!!!!")
    