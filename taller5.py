hombres = float(input("\ncuandos hombre ingresaron: "))
mujeres = float(input("\ncuandos mujeres ingresaron: "))

suma = hombres + mujeres 

print(f"\npersonas que ingresaron fue: {suma:,.0f}")

porcen1 = hombres / suma * 100 

print(f"\nPorcentaje de hombre es: {porcen1:,.1f}% ")

porcen2 = mujeres / suma * 100 

print(f"\nporcentaje de mujeres es: {porcen2:,.1f}%")

