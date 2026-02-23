alunos = [
    {"nome": "Ana", "notas": [8, 9, 7]},
    {"nome": "Bruno", "notas": [5, 4, 3]},
    {"nome": "Carlos", "notas": [10, 10, 10]},
    {"nome": "Diana", "notas": [6, 6, 6]}
]

primeiro_aluno = alunos[0]
nome = alunos[0]["nome"]
notas = alunos[0]["notas"]
primeira_nota = alunos[0]["notas"][0]

for aluno in alunos:
    print(f"Nome: {aluno['nome']} | Notas: {aluno['notas']}")

for i, aluno in enumerate(alunos, 1):
    print(f"Aluno {i}: {aluno['nome']}")

for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    print(f"{aluno['nome']:10} - Média: {media:.2f}")

aprovados = [aluno for aluno in alunos 
             if sum(aluno["notas"]) / len(aluno["notas"]) >= 7]
print(f"Alunos aprovados: {[a['nome'] for a in aprovados]}")

reprovados = [aluno for aluno in alunos 
              if sum(alunos['notas']) / len(alunos['notas'] > 7)]

alunos_ordenados = sorted(alunos, 
                         key=lambda x: sum(x["notas"]) / len(x["notas"]), 
                         reverse=True)

for i, aluno in enumerate(alunos_ordenados, 1):
    media = sum(aluno["notas"]) / len(aluno["notas"])
    print(f"{i}º - {aluno['nome']:10} - Média: {media:.2f}")

alunos_copia = [aluno.copy() for aluno in alunos]
for aluno in alunos_copia:
    aluno["notas"] = aluno["notas"].copy()

alunos_copia[0]["notas"].append(10)
print(f"Novas notas de Ana: {alunos_copia[0]['notas']}")

alunos_copia.append({"nome": "Eduardo", "notas": [7, 8, 9]})
print(f"Total de alunos após adicionar Eduardo: {len(alunos_copia)}")

def buscar_aluno(nome):
    for aluno in alunos:
        if aluno["nome"] == nome:
            return aluno
    return None

carlos = buscar_aluno("Carlos")
if carlos:
    print(f"Aluno encontrado: {carlos}")
else:
    print("Aluno não encontrado")

joao = buscar_aluno("João")
if joao:
    print(f"Aluno encontrado: {joao}")
else:
    print("Aluno 'João' não encontrado")

for aluno in alunos:
    maior = max(aluno["notas"])
    menor = min(aluno["notas"])
    print(f"{aluno['nome']:10} - Maior: {maior} | Menor: {menor}")

melhor_aluno = max(alunos, key=lambda x: sum(x["notas"]) / len(x["notas"]))
melhor_media = sum(melhor_aluno["notas"]) / len(melhor_aluno["notas"])

pior_aluno = min(alunos, key=lambda x: sum(x["notas"]) / len(x["notas"]))
pior_media = sum(pior_aluno["notas"]) / len(pior_aluno["notas"])

media_turma = sum(sum(a["notas"]) / len(a["notas"]) for a in alunos) / len(alunos)

for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    aluno["media"] = round(media, 2)
    aluno["status"] = "Aprovado" if media >= 7 else "Reprovado"

for aluno in alunos:
    print(f"{aluno['nome']:10} - Média: {aluno['media']} - {aluno['status']}")
