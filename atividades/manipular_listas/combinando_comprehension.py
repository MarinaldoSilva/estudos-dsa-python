
# 1. String Manipulation (upper, strip, replace)
nomes_sujos = ["  joao ", "maria", "  pedro  ", "ANA"]
nomes_limpos = [nome.strip().title() for nome in nomes_sujos]
print(f"1. Limpeza de Strings: {nomes_limpos}")

# 2. Type Conversion (str -> int/float)
valores_texto = ["10", "25", "50", "100"]
valores_numericos = [int(v) for v in valores_texto]
# Agora podemos somar!
soma = sum(valores_numericos) 
print(f"2. Conversão e Soma: {valores_numericos} (Soma: {soma})")

# 3. Filtering + Transformation (Modificar SÓ o que passar no filtro)
arquivos = ["dados.txt", "imagem.jpg", "relatorio.txt", "script.py"]
# Pegar apenas os .txt e deixar em MAIÚSCULO (sem a extensão)
docs = [arq.replace(".txt", "").upper() for arq in arquivos if arq.endswith(".txt")]
print(f"3. Filtro e Transformação: {docs}")

# 4. Usando ENUMERATE (Indice e Valor)
# Queremos formatar como "Item 1: Valor", "Item 2: Valor"...
frutas = ["Maçã", "Banana", "Uva"]
lista_formatada = [f"Item {i+1}: {fruta}" for i, fruta in enumerate(frutas)]
print(f"4. Com Enumerate: {lista_formatada}")

# 5. Usando FUNÇÕES PRÓPRIAS
def calcular_imposto(valor):
    return valor * 0.15

precos = [100, 200, 500]
impostos = [calcular_imposto(p) for p in precos]
print(f"5. Com Função Customizada: {impostos}")
