from collections import Counter

candidatos = [
    {"nome": "Alice", "experiencia": 3, "linguagens": ["Python", "SQL"]},
    {"nome": "Bruno", "experiencia": 1, "linguagens": ["Python", "JavaScript"]},
    {"nome": "Carla", "experiencia": 5, "linguagens": ["Java", "C++", "Python"]},
    {"nome": "Diego", "experiencia": 2, "linguagens": ["JavaScript", "HTML"]},
    {"nome": "Elena", "experiencia": 4, "linguagens": ["Python", "SQL", "Docker"]}
]

def filtrar_candidatos(lista_candidatos):
    lista_nomes = []
    
    for p in lista_candidatos:
        if p['experiencia'] >= 3 and "Python" in p['linguagens']:
            lista_nomes.append(p['nome'])
    return lista_nomes
    
    
def contar_linguagens(lista_candidatos):
    placar = {}
    
    for i in lista_candidatos:
        for j in i['linguagens']:
            if j in placar: 
                placar[j] = placar[j] + 1 #placar.get(j, 0) + 1
            else:
                placar[j] = 1
    return placar



def filtrar_candidatos_v2(lista_candidatos):
    """Mesma lógica, mas usando List Comprehension"""
    return [p['nome'] for p in lista_candidatos if p['experiencia'] >= 3 and "Python" in p['linguagens']]

def contar_linguagens_v2(lista_candidatos):
    """Refatorada usando o método .get() do dicionário."""
    placar = {}
    for i in lista_candidatos:
        for j in i['linguagens']:
            placar[j] = placar.get(j, 0) + 1
    return placar

def contar_linguagens_v3(lista_candidatos):
    """Refatorada usando a biblioteca nativa collections.Counter."""
    # Junta todas as linguagens numa única lista e depois conta
    todas_linguagens = [ling for cand in lista_candidatos for ling in cand['linguagens']]
    return dict(Counter(todas_linguagens))

# --- TESTES E COMPARAÇÕES ---
print("== TESTES FUNÇÕES ORIGINAIS ==")
print("Filtrar:", filtrar_candidatos(candidatos))
print("Contar: ", contar_linguagens(candidatos))

print("\n== TESTES FUNÇÕES REFATORADAS ==")
print("Filtrar V2:", filtrar_candidatos_v2(candidatos))
print("Contar V2: ", contar_linguagens_v2(candidatos))
print("Contar V3: ", contar_linguagens_v3(candidatos))
            
        