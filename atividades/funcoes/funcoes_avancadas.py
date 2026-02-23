import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

dados = [
    {"id": 1, "produto": "notebook ", "valor": "3000"},
    {"id": 2, "produto": "MOUSE", "valor": "50"},
    {"id": 3, "produto": "teclado", "valor": "100"},
    {"id": 4, "produto": "Mouse pad Rússia", "valor": "39.90"},
]

def limpar_dados(item):
    return {
        "id": item["id"],
        "produto": item["produto"].strip().title(),
        "valor": float(item["valor"])
    }
   
vendas = [limpar_dados(d) for d in dados]

print(f"saida: {vendas} " )

tabela_precos = {item["produto"]: item["valor"] for item in vendas}

busca = "Notebook"


if busca in tabela_precos:
    formatar_dados = json.dumps(tabela_precos, ensure_ascii=False, indent=4)
    print(formatar_dados)
