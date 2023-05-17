empredo = float(input("\n escrima la edad que tiene:  " ))
sueldo = float(input("sueldo del empleador"))

if empredo >= 55 :
    bono = round(sueldo * 0.15)
    total = bono + sueldo
    print(f"edad del empledo: {empredo:,.0f} y contara con un bono {bono:,.0f} mas su sueldo {sueldo:,.0f}")
    print(f"total a pagar {total:,.0f}")
else:
    
    print(f"sueldo de {sueldo:,.0f} y sin bono  ")


