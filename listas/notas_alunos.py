import json

alunos = [
    {"nome": "Ana", "notas": [8, 9, 7]},
    {"nome": "Bruno", "notas": [5, 4, 3]},
    {"nome": "Carlos", "notas": [10, 10, 10]},
    {"nome": "Diana", "notas": [6, 6, 6]}
]

situacao = [
    {"Nome": aluno['nome'],
    "Status": "Aprovado" 
        if sum(aluno['notas']) / len(aluno['notas']) >= 7 else "Reprovado"}
    for aluno in alunos
]

#print(json.dumps(situacao, indent=2))

relatorio_1 = [
    {
        **aluno,
        "status": "Aprovado" if sum(aluno['notas']) / len(aluno['notas']) >= 7 else "Reprovado"
    }
    for aluno in alunos
]
#print(json.dumps(relatorio_1, indent=2))

relatorio = [
    {
        "nome": aluno['nome'],
        "media" : sum(aluno['notas']) / len(aluno['notas']),
        "status" : "Aprovado" if sum(aluno['notas']) / len(aluno['notas']) >=7 else "Reprovado"
    }
    for aluno in alunos
]

#print(json.dumps(relatorio, indent=2, ensure_ascii=False))

def calcular_media(aluno):
    media = sum(aluno['notas']) / len(aluno['notas'])
    return {
        "nome": aluno['nome'],
        "media": media,
        "status": "Aprovado" if media >= 7 else "Reprovado"
    }
    
relatorio2 = [calcular_media(aluno) for aluno in alunos]
print(json.dumps(relatorio2, indent=2))