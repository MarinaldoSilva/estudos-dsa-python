precos_brutos = [100, -50, None, 200, 0, 300]

precos_positivos = [preco for preco in precos_brutos if preco is not None and preco > 0]
print(f"precos_positivos: {precos_positivos}") 
