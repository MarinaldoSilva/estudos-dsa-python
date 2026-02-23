salarios = [1500, 3000, 5000]

def calcular_salario_liquido(salario_bruto):
    if salario_bruto <= 2000:
        return salario_bruto - (salario_bruto * 0.10)
    else:
        return salario_bruto - (salario_bruto * 0.20)

for salario in salarios:
    liquido = calcular_salario_liquido(salario)
    print(f"salario Bruto: {salario} | liquido: {liquido}")
