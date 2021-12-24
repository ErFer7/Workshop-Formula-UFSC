# Resumo - Aula 3

## Tipos extras e outras estruturas

---

```python
# O valor "nenhum" ou "nulo" pode ser atribuido a uma variável.
# Isso poderia ser usado para inicializar um atributo em uma classe
# por exemplo.
# (Explicações detalhadas nas aulas) .
a = None

# Dicionários são estruturas que possuem chaves no lugar de índices.
b = {}                          # Dicionário vazio.
c = {"a" : 1, "b" : 2, "c": 3}  # Dicionário com 3 valores.

c["a"]  # Acessa o valor que estiver na chave "a".

c.keys()    # Retorna as chaves.
c.values()  # Retorna os valores.

# Tuplas são similares às listas, porém não podem ser modificadas.
d = (1, 2, 3)  # Tupla com 3 valores.

# Os conjuntos são estruturas que representam os dados sem repetição.
e = {1, 2, 3, 4}

# Operações com conjuntos:
# "a | b": União de "a" com "b".
# "a & b": Intercessão de "a" com "b".
# "a - b": Diferença de "a" com "b", tudo que está no "a" e não no "b".
# "b ^ a": Diferença simétrica de "a" com "b", tudo que não está na
# intercessão.

# Matrizes são representadas como listas dentro de outras listas.
a = []

# Este exemplo cria uma matriz de zeros.
for i in range(10):

    a.append([])

    for _ in range(10):
        a[i].append(0)
```

---

## Funções

```python
# Declaração de uma função:
def foo(arg):
    '''
    Esta função exibe o argumento no console.
    Este é um comentário que pode ser usado como
    documentação nas funções.
    '''

    print(arg)

# Exemplo:
# def <nome da função> (<argumentos>):
#   <corpo da função>

foo("argumento")  # Chama a função.

# Funções também podem retornar valores:
def func(x: float):  # float foi usado como uma anotação de documentação.
    return x ** 2 + 2 * x + 5

func(5)  # Retorna o resultado da operação com o x = 5.

# Lâmbdas podem ser interpretados como funções pequenas.
a = lambda x: x ** 2 + 2 * x + 5

a(5)  # Chama o lâmbda.
```

---

## Mapeamento, filtros, geradores e decoradores

```python
a = [n for n in range(10)]

# A função map aplica uma função em todos os elemetos. No exemplo
# os elementos estão sendo multiplicados por 2.
a = list(map(lambda x: x * 2, a))

b = [n for n in range(10)]

# A função filter retorna os elementos que se enquaram no critério da
# função passada. No exemplo a função passada é um lâmbda que retorna
# veradeiro se o número for par.
b = list(filter(lambda x: x % 2 == 0, b))

# Geradores são funções que podem gerar valores de forma personalizada.
# O exemplo abaixo é um gerador de números aleatórios.

from random import randint

def random_number_generator(length: int, start: int, end: int):
    '''
    Gera números aleatórios.
    '''

    for _ in range(length):
        # O yield é usado para retornar o valor e continuar a execução.
        yield randint(start, end)

# Exemplo do uso do gerador.
random_numbers = [n for n in random_number_generator(100, 0, 100)]

# Decoradores podem ser usados para compor alguns comportamentos com
# funções.

# Decorador.
def decor(func):

    # Função de empacotamento.
    def wrapper():
        print("Alguma coisa antes da função.")
        func()  # Função a ser decorada.
        print("Alguma coisa depois da função.")

    return wrapper

@decor           # Aplica o decorador à função.
def log_text():  # Função a ser decorada.
    print("Texto da função.")

log_text()  # Chamada da função a ser decorada.
```

---

## Recursão

```python
# É possível chamar uma função dentro de outra, isso é uma chamada
# recursiva.

# Exemplo de uma função recursiva que calcula o fatorial de um número.
def factorial(n: int):

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```
