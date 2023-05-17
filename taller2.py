#ventas del mes
venta1 = float(input("\ncual es el valor de la primera venta "))
venta2 = float(input("\ncual es el valor de la segunda venta "))
venta3 = float(input("\ncual es el valor de la tersera venta "))

#total ventas del mes 
suma = venta1+venta2+venta3
print(f"\nventas del mes {suma}")

#comision de 10% ventas 
comision = round((suma) * 0.10)
print(f"\ncomision del 10% {comision}  ")

# salario base 

print("\nsalario base $ 120000")

total = comision + 1200000 

print(f"\nsalario base mas comision  {total}")


