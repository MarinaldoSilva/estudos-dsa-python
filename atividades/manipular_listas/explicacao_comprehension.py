precos_brutos = [100, -50, None, 200]

print("--- EXPLICANDO LIST COMPREHENSION ---")

# 1. O PADRÃO (Funciona)
# Lógica: "Para cada item na lista (chamado 'p'), eu quero guardar esse mesmo 'p'"
lista1 = [p for p in precos_brutos if p is not None]
print(f"Caso 1 (Normal): {lista1}")

# 2. MUDANDO O NOME DA VARIÁVEL (Funciona)
# Lógica: O nome não importa, desde que "quem produz" (for) e "quem consome" (inicio) sejam iguais.
lista2 = [banana for banana in precos_brutos if banana is not None]
print(f"Caso 2 (Nome diferente): {lista2}")

# 3. O SEU EXEMPLO (ERRO)
# Lógica: O 'for' cria a variavel 'preco'. Mas o inicio tenta usar 'preco_final'.
# Como 'preco_final' não existe, dá erro.
print("\nTentando caso 3...")
try:
    lista3 = [preco_final for preco in precos_brutos if preco is not None]
except NameError as e:
    print(f"ERRO no Caso 3: {e}") 
    print("Explicação: O Python não sabe quem é 'preco_final'. Ele só conhece 'preco'")


# 4. CRIANDO UM 'PRECO_FINAL' (Funciona)
# Aqui, nós *criamos* o preço final usando o preço original.
# Lógica: "Pega o 'preco', multiplica por 2 (isso vira o valor final), e guarda."
lista4 = [preco * 2 for preco in precos_brutos if preco is not None]
print(f"\nCaso 4 (Transformação): {lista4}")
