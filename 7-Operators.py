x=301
x0=300
x1=304
x2=305
x3=307

y0=2.4771
y1=2.4829
y2=2.4843
y3=2.4871

print("\nLagrnge's inter ploating formula")
b1=(((x-x1)*(x-x2)*(x-x3)) / ((x0-x1)*(x0-x2)*(x0-x3)))*y0
b2=(((x-x0)*(x-x2)*(x-x3)) / ((x1-x0)*(x1-x2)*(x1-x3)))*y1
b3=(((x-x0)*(x-x1)*(x-x3)) / ((x2-x0)*(x2-x1)*(x2-x3)))*y2
b4=(((x-x0)*(x-x1)*(x-x2)) / ((x3-x0)*(x3-x1)*(x3-x2)))*y3

print(b1+b2+b3+b4,"\n")