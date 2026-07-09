num = int(input("Quantos termos você quer ver? "))
t1= 0
t2= 1
cont=0
while cont < num:
    print(t1, end="-")
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont+=1



