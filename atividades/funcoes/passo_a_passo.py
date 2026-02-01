import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
def mostra_passo_a_passo():
    precos = [100, -50, 200]

    nova_lista = []
    
    for p in precos:
        preco = p
        
        verifica_preco = (preco > 0)
        
        if verifica_preco:
            valor_final = preco 
            
            nova_lista.append(valor_final)
        else:
            print(f"Preço não positivo: {preco}")
        
    format_list = json.dumps(nova_lista, indent=4, ensure_ascii=False)
    print(format_list)

if __name__ == "__main__":
    mostra_passo_a_passo()
