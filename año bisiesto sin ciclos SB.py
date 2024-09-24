def es_bisiesto(año):
    return (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0))

def contar_años_bisiestos(year):
    return sum(1 for año in range(1900, year + 1) if es_bisiesto(año))

año_respondido = int(input("escribe un año entre 1900 y 2199 "))
if 1900 <= año_respondido <= 2199:
    bisiestos = contar_años_bisiestos(año_respondido)
    print(f"numero de años bisiestos hasta {año_respondido}: {bisiestos}")
else:
    print("no estas en el rango")