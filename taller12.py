resp = "si"  
while resp == "si" :
    nom1 = input("Nombre del estuduante: ")
    par1 = float(input("Digite la calificación 1: "))
    par2 = float(input("Digite la calificación 2: "))
    par3 = float(input("Digite la calificación 3: "))
    par4 = float(input("Digite la calificación 4: "))
    par5 = float(input("Digite la calificación 5: "))
    pro1 = round(( par1 + par2 + par3 + par4 + par5) / 5)

    nom2 = input("Nombre del estuduante: ")
    par1 = float(input("Digite la calificación 1: "))
    par2 = float(input("Digite la calificación 2: "))
    par3 = float(input("Digite la calificación 3: "))
    par4 = float(input("Digite la calificación 4: "))
    par5 = float(input("Digite la calificación 5: "))
    pro2 = round(( par1 + par2 + par3 + par4 + par5) / 5)

    nom3 = input("Nombre del estuduante: ")
    par1 = float(input("Digite la calificación 1: "))
    par2 = float(input("Digite la calificación 2: "))
    par3 = float(input("Digite la calificación 3: "))
    par4 = float(input("Digite la calificación 4: "))
    par5 = float(input("Digite la calificación 5: "))
    pro3 = round(( par1 + par2 + par3 + par4 + par5) / 5)

    if pro1 >= 3.0 : #or pro2 >= 3.0:
         estado = "Aprobado"
    else:
        estado = "Reprobado"

    if  pro2 >= 3.0:         
            estado2 = "Aprobado"
    else:
            estado2 = "Reprobado"    
    
    if  pro3 >= 3.0:         
            estado3 = "Aprobado"
    else:
            estado3 = "Reprobado" 

    input(f"el estudiante: {nom1} su promedio es: {pro1}  a:{estado}")
    input(f"el estudiante: {nom2} su promedio es: {pro2}  a:{estado2}")
    input(f"el estudiante: {nom3} su promedio es: {pro3}  a:{estado3}")

    resp = input("Comensar a calificar otra ves: ")



        