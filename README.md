# 📚 Estrutura de Dados com Python

Este repositório contém exercícios práticos e estudos relacionados a **Estruturas de Dados** utilizando a linguagem **Python**. O foco principal deste projeto é trabalhar com **listas sequenciais**, **ordenação de dados** e o conceito de **classes**. Cada exercício busca consolidar os conceitos e práticas de manipulação de dados e objetos.

---

## 🚀 Objetivos do Projeto

* Compreender a manipulação de **listas sequenciais** em Python.
* Implementar algoritmos de **ordenação de listas**.
* Trabalhar com **orientação a objetos**, utilizando **classes** e **métodos**.
* Aplicar **operações matemáticas** em listas, como somas e médias.

---

## 🗂️ Estrutura do Projeto

ESTRUTURA-DE-DADOS/
├── exercicios/
├── ex2ED_Class/
├── ex3LTS_Sequencial/
├── ex4Ordenaça/
└── README.md

---

## 🧑‍💻 Conceitos e Atividades Práticas

## 🏦 1. Classes e Objetos

* **Objetivo**: Implementar uma classe `ContaBancaria` para simular o cálculo de saldo e extrato bancário.
* **Descrição**:
  - A classe `ContaBancaria` recebe o saldo inicial e o nome do titular.
  - Métodos para calcular as entradas e saídas, e mostrar o resultado do saldo.

📌 **Conceitos aplicados:**
  - Definição de classe e atributos em Python.
  - Métodos de instância para manipular e exibir dados.
  - Construtores e o uso de `self`.

```python
class ContaBancaria:
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular

    def calculo_entrada(self):
        self.entrada = self.saldo
        return self.entrada
    
    def calculo_saida(self):
        self.saida = self.saldo - self.entrada
        return self.saida
    
    def mostrar_resultado(self):
        print(f'Valor em conta: {self.entrada}')
        print(f'Extrato de saídas: {self.saida}')

saldo = ContaBancaria(5000, "Kevin")
print('Saldo em conta corrente:', saldo.calculo_entrada())
saldo.calculo_saida()
```

---

### 📝 2. **Listas Sequenciais**

* **Objetivo**: Criar uma lista de números gerados aleatoriamente e calcular a média desses números.
* **Descrição**: 
    - Utilizando a biblioteca `random` para gerar números aleatórios entre 0 e 50.
    - A lista é populada e, posteriormente, é calculada a média dos valores.

📌 **Conceitos aplicados**:
  - Manipulação de listas em Python.
  - Operações matemáticas: soma e cálculo de média.
  - Uso de laços de repetição (`for`) e contadores.

```python
from random import randint

numeros = []
soma = 0
contador = 0
qnt = int(input("A lista deve conter quantos números? "))

for i in range(qnt):
    num = randint(0, 50)
    numeros.append(num)

for n in numeros:
    soma += n
    contador += 1

media = soma / contador
print(f"Os números gerados foram {numeros}.")
print(f"A média dos valores é {media:.2f}.")
```

## 🔄 3. Ordenação de Listas
* **Objetivo**: Ordenar uma lista de números aleatórios em ordem decrescente.
* **Descrição**:
  - Utilizando o algoritmo de seleção para ordenar a lista em ordem decrescente.
  - O código encontra o terceiro maior número da lista ordenada.

📌 **Conceitos aplicados:**
  - Algoritmo de ordenação Seleção.
  - Manipulação de listas.
  - Uso de laços de repetição (`for`), controle de fluxo e troca de valores.

```python
from random import randint

def decrescente(lista_vetor):
    for i in range(len(lista_vetor)):
        menor_index = i
        for j in range(i+1, len(lista_vetor)):
            if lista_vetor[j] > lista_vetor[menor_index]:
                menor_index = j
        lista_vetor[i], lista_vetor[menor_index] = lista_vetor[menor_index], lista_vetor[i]

n = int(input("Quantos valores deve haver no vetor? "))
lista_vetor = []

for  i in range(0, n):
    lista_vetor.append(randint(1, 20))

print(f"Lista original: {lista_vetor}")
decrescente(lista_vetor)

terceiro_maior = lista_vetor[2]
print(f"O terceiro maior valor é: {terceiro_maior}")
```

## 🛠️ Tecnologias e Ferramentas

* **Python** (3.x)
* **IDE**: VSCode, PyCharm ou Jupyter Notebook.
* **Ferramentas**: Git, GitHub para controle de versão.

## 📌 Considerações Finais
Este repositório foi criado com o intuito de aprofundar o conhecimento sobre Estruturas de Dados em Python. Através dos exercícios práticos, é possível compreender como manipular listas, ordenar dados e trabalhar com orientação a objetos de forma eficiente.

A prática desses conceitos ajudará a aprimorar suas habilidades em algoritmos, estruturas de dados e programação orientada a objetos, fundamentais para o desenvolvimento de software mais eficiente.

“Entender a estrutura e a organização dos dados é a chave para criar soluções poderosas e escaláveis.”
