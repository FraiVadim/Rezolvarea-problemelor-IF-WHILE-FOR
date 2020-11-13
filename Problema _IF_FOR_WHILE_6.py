n=eval(input("dati n: "))
s1=0
s2=0
x=0
r=0
s=0
p=0
for i in range (1,n+1):
    s1+=i**3  
i=0    
for i in range (1,n+1):
    x+=i
    s2=x**2  
i=0
if s1>s2 :
    print("a.)s1 mai mare ca s2")
if s1==s2 :
    print("a.)sunt egale")
else :
    print("a.)s2 mai mare ca s1")
s1=0
s2=0


for i in range (1,n+1):
    r+=i**2
    s1=n*r  
i=0    
for i in range (1,n+1):
    s+=i
    p+=n**(i)
    s2=s+p-n
if s1>s2 :
    print("b.)s1 mai mare ca s2")
if s1==s2 :
    print("b.)sunt egale")
else :
    print("b.)s2 mai mare ca s1")