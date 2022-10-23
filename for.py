sayac=0
sayi=input("sayı: ")
for i in range(2,int(sayi)):
    if(int(sayi)%i==0):
        sayac+=1
        break
if(sayac!=0):
    print("sayı asal değildir.")
else:
    print("sayı asaldır.")