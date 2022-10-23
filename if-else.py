vize = float(input("vize: "))
final = float(input("final: "))
proje = float(input("proje: "))

ort = (vize+final+proje)/3
if(ort>=0) and (ort<25):
    print(f"ortalamanız: {ort} notunuz: 0")
elif(ort>=25) and (ort<45):
    print(f"ortalamanız: {ort} notunuz: 1")
elif(ort>=45) and (ort<55):
    print(f"ortalamanız: {ort} notunuz: 2")    
elif(ort>=55) and (ort<70):
    print(f"ortalamanız: {ort} notunuz: 3")
elif(ort>=70) and (ort<85):
    print(f"ortalamanız: {ort} notunuz: 4")      
elif(ort>=85) and (ort<=100):
    print(f"ortalamanız: {ort} notunuz: 5")   
else:
    print("yanlış bilgi girdiniz...")   
