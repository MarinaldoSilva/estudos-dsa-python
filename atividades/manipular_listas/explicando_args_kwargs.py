
# Vamos imaginar que estamos pedindo um sanduíche no Subway.

# *ARGS (Ingredientes Soltos):
# São coisas que você vai pedindo "um monte", sem precisar dar nome.
# "Bota queijo, tomate, alface, picles..." -> Isso vira uma LISTA (tupla) de coisas.

# **KWARGS (Opções com Nome/Etiqueta):
# São configurações específicas que precisam de nome.
# "molho=picante", "tamanho=30cm", "para_viagem=Sim" -> Isso vira um DICIONÁRIO.

def montar_sanduiche(*ingredientes, **opcoes):
    print("\n--- INICIANDO PEDIDO ---")
    
    # 1. PROCESSANDO OS ARGS (A Lista de Ingredientes)
    # O Python pega tudo que veio solto e joga numa Tupla chamada 'ingredientes'
    print(f"Ingredientes (ARGS): {ingredientes}")
    
    if not ingredientes:
        print(" -> O sanduíche está vazio!")
    else:
        for item in ingredientes:
            print(f" -> Adicionando: {item}")
            
    # 2. PROCESSANDO OS KWARGS (As Opções Específicas)
    # O Python pega tudo que veio com 'nome=valor' e joga num Dict chamado 'opcoes'
    print(f"\nOpções Extras (KWARGS): {opcoes}")
    
    # Podemos buscar chaves específicas no dicionário
    if "molho" in opcoes:
        print(f" -> Molho escolhido: {opcoes['molho']}")
    
    if opcoes.get("viagem") == True:
        print(" -> EMPACOTAR PARA VIAGEM!")

# CHAMADA 1: Só ingredientes (Args)
montar_sanduiche("Queijo", "Presunto")

# CHAMADA 2: Ingredientes (Args) + Opções (Kwargs)
montar_sanduiche("Frango", "Bacon", "Alface", molho="Barbecue", viagem=True)
