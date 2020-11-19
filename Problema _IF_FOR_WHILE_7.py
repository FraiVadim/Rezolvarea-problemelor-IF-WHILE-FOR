n=int(input("dati virsta lui Mihai: "))
suma=1
v=1
if n<20:
    for i in range (1,n+1):
        suma=(suma*2)+i  
print("suma=",suma)
suma=1
for i in range (1,21):
    if suma<100:
        suma=(suma*2)+i  
    else :
        print("suma mai mare de 100 la",i-1,"ani") 
        break
    
      



