n=int(input("dati numarul: "))
m=int(input("dati numarul: "))
while (n%m)==0 :
     n/=m
if n==1:
    print("da")
else :
    print("nu")