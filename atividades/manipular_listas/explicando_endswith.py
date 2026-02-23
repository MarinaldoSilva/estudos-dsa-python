
# O que é o .endswith()?
# É uma PERGUNTA que você faz para um texto.
# A resposta é sempre SIM (True) ou NÃO (False).

arquivo1 = "foto.jpg"
arquivo2 = "notas.txt"

print(f"O arquivo '{arquivo1}' termina com .txt?")
resposta = arquivo1.endswith(".txt")
print(f"RESPOSTA: {resposta}")  # Vai dar False

print(f"\nO arquivo '{arquivo2}' termina com .txt?")
resposta = arquivo2.endswith(".txt")
print(f"RESPOSTA: {resposta}")  # Vai dar True

print("\n--- COMO O IF USA ISSO ---")
# O 'if' só deixa passar o que for True.

lista = ["foto.jpg", "notas.txt", "script.py", "lista.txt"]

print(f"Lista original: {lista}")
print("Filtrando apenas .txt...")

for item in lista:
    # A PERGUNTA MÁGICA
    eh_txt = item.endswith(".txt")
    
    if eh_txt == True:
        print(f" - {item}: PASSOU (é True)")
    else:
        print(f" - {item}: BARRADO (é False)")
