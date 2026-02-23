# Explicando as Combinações de List Comprehension

Aqui está a explicação "passo a passo" para cada um dos exemplos do arquivo `combinando_comprehension.py`, usando a nossa lógica da **Fábrica** (Loop) e da **Montagem** (Início).

---

## 1. Limpeza de Strings (Métodos `.strip().title()`)
```python
[nome.strip().title() for nome in nomes_sujos]
```
*   **Fábrica (`for nome in nomes_sujos`)**: Pega um nome sujo (ex: `"  joao "`) e coloca na caixa temporária `nome`.
*   **Montagem (`nome.strip().title()`)**:
    1.  O operário pega a caixa `nome`.
    2.  Primeiro passa um pano (`strip`) -> vira `"joao"`.
    3.  Depois arruma a primeira letra (`title`) -> vira `"Joao"`.
    4.  Só agora guarda na lista final.

## 2. Conversão de Tipos (Função `int()`)
```python
[int(v) for v in valores_texto]
```
*   **Fábrica (`for v in valores_texto`)**: Pega o texto (ex: `"10"`) e chama de `v`.
*   **Montagem (`int(v)`)**:
    1.  O operário pega o texto `v`.
    2.  Joga numa máquina transformadora (`int()`) que converte texto em número.
    3.  O que sai da máquina (o número `10`) é o que vai para a lista final.

## 3. Filtro e Transformação (Métodos + `if`)
```python
[arq.replace(".txt", "").upper() for arq in arquivos if arq.endswith(".txt")]
```
*   **Fábrica (`for arq in arquivos`)**: Pega um nome de arquivo (ex: `"dados.txt"`).
*   **Controle de Qualidade (`if arq.endswith(".txt")`)**:
    *   O inspetor olha: "Termina com .txt?".
    *   Se **NÃO**: Joga fora (ignora "imagem.jpg").
    *   Se **SIM**: Passa adiante ("dados.txt" passa).
*   **Montagem (`arq.replace(...).upper()`)**:
    1.  Pega o aprovado `"dados.txt"`.
    2.  Arranca o final (`replace`) -> vira `"dados"`.
    3.  Grita (`upper`) -> vira `"DADOS"`.
    4.  Guarda `"DADOS"` na lista.

## 4. Usando `enumerate` (Índice e Valor)
```python
[f"Item {i+1}: {fruta}" for i, fruta in enumerate(frutas)]
```
*   **Fábrica Dupla (`for i, fruta in enumerate...`)**:
    *   Dessa vez, a esteira traz **duas coisas** juntas numa bandeja: o número da posição (0, 1, 2...) e a fruta.
    *   A gente dá apelido pra cada um: `i` pro número, `fruta` pra fruta.
*   **Montagem (`f"Item {i+1}: {fruta}"`)**:
    1.  O operário pega o `i` (ex: 0), soma 1 (vira 1).
    2.  Pega a `fruta` (ex: "Maçã").
    3.  Monta uma frase bonitinha usando os dois.
    4.  Guarda a frase pronta.

## 5. Função Customizada
```python
[calcular_imposto(p) for p in precos]
```
*   **Fábrica (`for p in precos`)**: Pega o preço bruto (ex: 100) e chama de `p`.
*   **Montagem (`calcular_imposto(p)`)**:
    1.  Em vez de fazer o trabalho ali mesmo, o operário manda o `p` para um departamento terceirizado (`def calcular_imposto`).
    2.  Fica esperando...
    3.  O departamento devolve o resultado (15.0).
    4.  O operário guarda esse 15.0 na lista final.
