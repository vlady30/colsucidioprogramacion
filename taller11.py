resp = "si"
while  resp == "si":

    sueldo = float(input("cual es tu salario: "))

    if  sueldo <= 655000: 
        bono = sueldo * 0.04 
        total = sueldo + bono
        input(f"Su sueldo es:${sueldo} mas bonificacion de:${bono:,.1f} total a pagar es:$ {total}")
       # resp = input("¡¿Desea iniciar otra ves?")

    else:            
        input(f" Su sueldo a pagar es:${sueldo} y no tienes bonificacion este mes  ")      
    resp = input("¡¿Desea iniciar otra ves?: ")

      
