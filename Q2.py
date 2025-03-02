D=int(input("the number of donuts available when the shop first opens: "))
E=int(input("the number of events that happen over the course of the day: "))
lst_V=[]
lst_Q=[]
for i in range(E):
    V=0
    Q=0
    V=input("donuts have been baked/sold: ")
    lst_V.append(V)
    Q=int(input("the quantity of donuts associated with the event: "))
    lst_Q.append(Q)
for i in range(E):
    if lst_V[i]=="+":
        D=D+lst_Q[i]
    if lst_V[i]=="-":
        D=D-lst_Q[i]
print(D)