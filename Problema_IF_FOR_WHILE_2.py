m=1
k=0
n=int(input("dati numarul "))
if n>1:
    for i in range(1,n+1):
        m*=i
        k+=m
print (k)