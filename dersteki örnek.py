n=int(input("kat adet sayı girilecek: "))
a=[]
for i in range(0,n):
    elem=int(input("sayıyı girin: "))
    a.append(elem)
avg=sum(a)/n
print("girilen sayıların ortalaması : ", round(avg,2))


