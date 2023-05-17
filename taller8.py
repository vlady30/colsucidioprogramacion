sueldo = float(input("cual es  tu sueldo basico:$"))
 
if sueldo >= 100000 and sueldo <= 150000:
    bono = sueldo * 0.02      
    print(f"su sueldo es {sueldo} mas bono del 2%{bono}")
elif sueldo >= 150001 and sueldo <= 200000:
    bono2 = sueldo * 0.05 
    print(f"su sueldo es {sueldo} mas bono del 5% {bono2}")    
else:
    print("no te corresponde  bono ")     
