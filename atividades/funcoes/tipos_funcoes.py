import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

def registrar_log(mensagem, historico=None):
    if historico is None:
        historico = []
    historico.append(mensagem)
    return historico

user_1 = registrar_log("Erro de conexão")

user_2 = registrar_log("Senha incorreta")

print("-"*40)
print(user_2)
print("-"*40)

def referencia_ou_valor():
    
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    resultado = {
        "1: a == b (valores iguais?)": a == b,
        "2: a is b (mesmo objeto?)": a is b,
        "3: a is c (mesmo objeto?)": a is c,
    }

    x = 256
    y = 256
    resultado["4: x is y"] = x is y

    z = 300
    w = 300
    resultado["5: z is w"] = z is w
    
    return resultado
    
saida = json.dumps(referencia_ou_valor(), ensure_ascii=False, indent=4)
print(saida)