# MaxMin Select

##  Descrição do Projeto

Este projeto implementa o algoritmo de **Seleção Simultânea do Maior e do Menor Elemento (MaxMin Select)**, utilizando a abordagem de **Divisão e Conquista**. O objetivo principal é otimizar a busca simultânea pelo menor e pelo maior valor dentro de um conjunto de números, reduzindo o número de comparações em relação a abordagens mais simples.

---

##  Estrutura do Projeto

O repositório contém os seguintes arquivos:

📂 **FPAAProjeto2** (Pasta do projeto)
   - 📄 `main.py` → Implementação do algoritmo MaxMin Select
   - 📄 `test_maxmin_select.py` → Testes unitários com `unittest`
   - 📄 `README.md` → Documentação detalhada

---

##  Como Executar o Projeto

###  Clonar o repositório
```bash
git clone https://github.com/gabrielfaria13/FPAAProjeto2.git
cd FPAAProjeto2
```

###  Executar o código principal
```bash
python main.py
```

###  Rodar os testes automatizados
```bash
python -m unittest test_maxmin_select.py
```
---

##  Explicação do Algoritmo

O **MaxMin Select** encontra simultaneamente o maior e o menor elemento de uma lista de forma otimizada. Ele segue a abordagem **Divisão e Conquista**, onde:

1️ Separa o problema em subproblemas menores.

2️ Resolve cada subproblema recursivamente.

3️ Combina os resultados para formar a solução final.

###  Implementação do Algoritmo

Abaixo está a implementação do algoritmo em **Python**:

```python
def maxmin_select(arr, left, right):
    if left == right:
        return arr[left], arr[right]
    elif right == left + 1:
        return (arr[left], arr[right]) if arr[left] < arr[right] else (arr[right], arr[left])
    
    mid = (left + right) // 2
    min1, max1 = maxmin_select(arr, left, mid)
    min2, max2 = maxmin_select(arr, mid + 1, right)
    
    return min(min1, min2), max(max1, max2)
```



###  Exemplo de Entrada e Saída

####  Entrada:
```python
arr = [3, 1, 8, 5, 2, 9, 4, 7]
print(maxmin_select(arr, 0, len(arr) - 1))
```

####  Saída:
```bash
(1, 9)
```

---

##  Análise de Complexidade Assintótica

###  Contagem de Operações
O algoritmo divide recursivamente o array até que os subproblemas contenham um ou dois elementos. Para cada divisão:
- Ele divide o array ao meio, criando dois subproblemas de tamanho \( n/2 \).
- Após cada chamada recursiva, são feitas **duas comparações** para combinar os resultados.

A recorrência associada ao número de comparações \( C(n) \) pode ser expressa como:

\[ C(n) = 2C(n/2) + 2 \]

Com os casos base:
\[ C(2) = 1 \]  (uma comparação entre dois elementos)
\[ C(1) = 0 \]  (um único elemento já é min e max)

###  Total de Comparações para \( n \) elementos:

Expandindo a recorrência:

\[ C(n) = 2C(n/2) + 2 \]
\[ C(n/2) = 2C(n/4) + 2 \]
\[ C(n/4) = 2C(n/8) + 2 \]

E assim por diante, até \( C(1) = 0 \).

Somando os termos, o total de comparações cresce linearmente, resultando em:

\[ C(n) = 3n/2 - 2 \]

Portanto, a complexidade assintótica é **O(n)**.

---

###  Aplicação do Teorema Mestre
A recorrência do tempo de execução tem a forma:

\[ T(n) = 2T(n/2) + O(1) \]

Comparando com a forma padrão do **Teorema Mestre**:

\[ T(n) = aT(n/b) + O(n^d) \]

Temos:
- **1. Identificação dos parâmetros:**
  - \( a = 2 \)
  - \( b = 2 \)
  - \( f(n) = O(1) \)

- **2. Cálculo de \( log_b(a) \):**

\[ log_2(2) = 1 \]

- **3. Comparação com \( d \):**
  - Aqui, \( d = 0 \) (pois o trabalho adicional é constante \( O(1) \)).
  - Como \( d = 0 < log_b(a) = 1 \), aplicamos o **Caso 1** do Teorema Mestre.

- **4. Solução Assintótica:**

\[ T(n) = O(n) \]

Ou seja, a complexidade final do algoritmo é **O(n)**.

---

##  Testes Automatizados

Para garantir a precisão do algoritmo, utilizamos **unittest**. O arquivo `test_maxmin_select.py` contém os seguintes testes:

- **Testa um único elemento**
- **Testa dois elementos**
- **Testa múltiplos elementos misturados**
- **Testa listas ordenadas e inversamente ordenadas**

###  Como rodar os testes
```bash
python -m unittest test_maxmin_select.py
```

---

##  Ponto Extra: Diagrama Visual

<img width="688" alt="image" src="https://github.com/user-attachments/assets/1c22c883-d1eb-4099-9fd3-9a81e0eae12d" />


Diagrama Visual do algoritmo MaxMin Select, demonstrando a abordagem de Divisão e Conquista. A imagem destaca o processo de divisão do conjunto original em partes menores, a busca simultânea pelo menor e maior valor em cada subdivisão e a combinação dos resultados para obter a solução final de forma otimizada.

---

## Conclusão

O algoritmo **MaxMin Select** demonstra uma abordagem eficiente para encontrar simultaneamente o menor e o maior elemento de um array. Utilizando a técnica de **Divisão e Conquista**, ele reduz significativamente o número de comparações necessárias, tornando a busca mais eficiente do que abordagens convencionais. 

A análise detalhada da complexidade assintótica comprova que o algoritmo possui desempenho **linear, O(n)**, sendo adequado para conjuntos de dados grandes. Além disso, os testes automatizados garantem a precisão e robustez da implementação, assegurando sua confiabilidade para diferentes cenários.


---
