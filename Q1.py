a=int(input("your place in line: "))
b=int(input("the number of cars the train has: "))
c=int(input("the number of people a single car holds: "))
d=a-b*c
if d<=0:
    print("yes")
else:
    print("no")
