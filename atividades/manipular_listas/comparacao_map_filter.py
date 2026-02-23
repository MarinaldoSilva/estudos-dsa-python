
# --- PARTE 1: MAP vs LIST COMPREHENSION ---
# O "Map" é como um carimbo: ele passa em TODOS os itens e aplica uma mudança.
# Imagine que você quer DOBRAR todos os números.

numeros = [1, 2, 3, 4]

# JEITO ANTIGO (Map):
# map(FUNÇÃO_QUE_TRABALHA, LISTA_DE_ITENS)
# Precisamos usar 'lambda' (uma função anônima/descartável) para dizer "pegue x e faça x * 2"
# E ainda precisamos converter para list() no final, senão o Python só cria um "agendamento".
map_obj = list(map(lambda x: x * 2, numeros))
print(f"1. Map (Antigo): {map_obj}")

# JEITO NOVO (Comprehension):
# É direto: "[ RESULTADO for ITEM in LISTA ]"
# Não precisa de lambda, nem de list(). É mais "limpo".
comp_obj = [x * 2 for x in numeros]
print(f"1. Comprehension (Novo): {comp_obj}")


# --- PARTE 2: FILTER vs LIST COMPREHENSION ---
# O "Filter" é uma peneira: ele só deixa passar o que for Verdadeiro.

# JEITO ANTIGO (Filter):
# filter(FUNÇÃO_TESTE, LISTA)
# A função DEVE retornar True ou False.
filter_obj = list(filter(lambda x: x > 2, numeros))
print(f"\n2. Filter (Antigo): {filter_obj}")

# JEITO NOVO (Comprehension):
# A peneira vira um simples 'if' no final.
comp_filter = [x for x in numeros if x > 2]
print(f"2. Comprehension (Novo): {comp_filter}")


# --- PARTE 3: HASH MAPS (DICIONÁRIOS) ---
# Você perguntou sobre "Hash". Em Python, "Hash Map" = "Dicionário" (Dict).
# É uma lista de pares CHAVE: VALOR.

chaves = ["nome", "idade", "cidade"]
valores = ["Tiringa", 70, "Serra Talhada"]

# DICT COMPREHENSION (A Mágica):
# Em vez de [], usamos {}.
# Em vez de um valor só, colocamos CHAVE: VALOR.

# 'zip(chaves, valores)' junta as duas listas par-a-par:
# ("nome", "Tiringa"), ("idade", 70)...
meu_hash_map = {chave: valor for chave, valor in zip(chaves, valores)}

print(f"\n3. Hash Map Gerado: {meu_hash_map}")
# Agora o acesso é imediato (O(1)) pelo nome da chave, isso é o poder do Hash.
print(f"   Acessando a chave 'cidade': {meu_hash_map['cidade']}")
