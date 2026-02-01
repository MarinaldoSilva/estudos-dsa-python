import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

estoque = {
    "camisa": {"preco": 39.90, "quantidade": 12},
    "calça": {"preco": 99.90, "quantidade": 75},
    "sapato": {"preco": 125.90, "quantidade": 23},
    "bone": {"preco": 29.90, "quantidade": 110},
}

vendas = []
clientes = set()

def formatar_texto(texto: str) -> str:
    return texto.lower().strip()

def realizar_venda(nome_cliente: str, produto: str, quantidade: int):
    cliente_formatado = formatar_texto(nome_cliente)
    produto_formatado = formatar_texto(produto)
    
    if produto_formatado not in estoque:
        print(f"Erro: O item '{produto}' não está disponível.")
        return

    dados_produto = estoque[produto_formatado]
    
    if quantidade <= 0:
        print("Erro: A quantidade deve ser maior que zero.")
        return

    if dados_produto["quantidade"] < quantidade:
        print(f"Estoque insuficiente para '{produto}'. Disponível: {dados_produto['quantidade']}")
        return

    dados_produto['quantidade'] -= quantidade
    clientes.add(cliente_formatado)
    
    venda = {
        "cliente": cliente_formatado,
        "produto": produto_formatado,
        "quantidade": quantidade,
        "total": dados_produto['preco'] * quantidade
    }
    vendas.append(venda)

    print(f"Venda realizada: {quantidade}x {produto} para {nome_cliente}")
    print(f"Novo estoque de {produto}: {dados_produto['quantidade']}")
    
    print("-" *40)
    print(json.dumps(estoque, indent=4, ensure_ascii=False))
    print("-" *40)

realizar_venda("Mario", "camisa", 10)
realizar_venda("Luigi", "calça", 2)