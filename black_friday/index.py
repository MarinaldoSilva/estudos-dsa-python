import logging
import json

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

estoque_galpao = {
    "notebook": {"preco": 3500.00, "quantidade": 5},
    "mouse": {"preco": 150.00, "quantidade": 20},
    "teclado": {"preco": 300.00, "quantidade": 0},
    "headset": {"preco": 400.00, "quantidade": 2}
}

carrinho_cliente = [
    {"produto": "notebook", "qtd": 2},
    {"produto": "mouse", "qtd": 5},
    {"produto": "teclado", "qtd": 1},
    {"produto": "monitor", "qtd": 2},
    {"produto": "headset", "qtd": 5}
]

def processar_pedido(estoque:dict, carrinho_cliente:list):
    logging.info(f"Iniciando processamento de {len(carrinho_cliente)} itens.")

    valor_total = 0
    erros = []
    
    for item in carrinho_cliente:
        item_nome = item['produto']
        item_qtd = item['qtd']
        
        logging.info(f"Analisando item: {item_nome} (Qtd Pedida: {item_qtd})")
        
        if item_nome in estoque:
            estoque_atual = estoque[item_nome]['quantidade']
            
            if estoque_atual >= item_qtd:
                logging.info(f"Tem estoque: {item_nome} - estoque: {estoque_atual}")
                
                dinheiro_deste_item = registrar_venda(estoque, item_nome, item_qtd)
                valor_total += dinheiro_deste_item
                
            else:
                logging.warning(f"{item_nome} sem estoque suficiente.")
                erros.append(item_nome)
                print(f"Sem estoque suficiente de: {item_nome}")
        else:
            logging.error(f"{item_nome} não encontrado.")
            erros.append(item_nome)
            print(f"Produto não existe no estoque: {item_nome}")
            
    return f"Valor Total Vendido: R$ {valor_total:.2f}. Erros: {erros}"

def registrar_venda(estoque, nome_item, qntd_comprada):
    preco_unidade = estoque[nome_item]['preco']
    custo = preco_unidade * qntd_comprada
    estoque[nome_item]['quantidade'] -= qntd_comprada
    return custo

print(processar_pedido(estoque_galpao, carrinho_cliente))
    
    
    
    
        
        