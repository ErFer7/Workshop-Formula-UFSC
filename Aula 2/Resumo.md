# Resumo - Aula 2

## Strings

---

```python

# Strings representam textos e podem ser definidos com o uso de aspas ou apóstrofos.
a = "Isso é um string"
b = 'Isso também é um string'

# É possível usar caracteres especiais para adicionar uma nova linha.
c = 'Primeira linha\nSegunda linha'

# A contra-barra é usada para fazer o "escape" de caracteres que
# normalmente seriam reconhecidos como parte da linguagem.
# "\'" irá ser exibido como "'" no console e "\\" será exibido como "\".
d = 'Caractere de escape: \', \\'

# É possível concatenar strings com o operador de soma.
# Resultado: String 1, String 2.
e = 'String 1, ' + 'String 2.'

# É possível multiplicar o string por um número. O exemplo abaixo produz
# f = "ababababab"
f = 'ab' * 5
```

---

## Input

```python
# É possível coletar o input do usuário desta forma.
a = input()

# Desta forma o programa irá exibir uma mensagem no input.
b = input('Insira alguma coisa: ')

# Conversão do input de um string para inteiro.
c = int(input())

# A forma abaixo usa a função split para dividir o string de input em uma
# lista.
d = input().split()

# É possível usar a função map para converter uma série de números
# inseridos. O input é dividido em uma lista de strings que são
# convertidos para inteiros com a função map.
e = map(int, input().split())
```

---

## Estruturas de decisão

```python
# Um bloco if/else checa se a condição é verdadeira e executa o que estiver
# no "if" caso seja, caso contrário o "else" será executado.
if  2 + 2 == 4:
    print('A matemática ainda funciona.')
else:
    print('A matemática não está funcionando.')

# Operadores condicionais:
# "a == b": checa se "a" é igual a "b".
# "a != b": checa se "a" é diferente de "b".
# "a > b": checa se "a" é maior que "b".
# "a < b": checa se "a" é menor que "b".
# "a >= b": checa se "a" é maior ou igual a "b".
# "a <= b": checa se "a" é menor ou igual a "b".

# O exemplo a baixo usa o elif. O elif significa "else if" e é executado
# caso a condição anterior não seja executada e a condição atual seja
# satisfeita. Quando um bloco if/elif/else é executado o programa continua
# para um ponto depois do else.

num = int(input())

if  num > 10:
    print('num é maior que 10.')
elif num > 5:
    print('num é maior que 5 e menor ou igual a 10.')
else:
    print('num é menor ou igual a 5.')

# É possível usar "and", "or" e "not" para fazer operaões lógicas.
# "a and b": Executa se "a" e "b" forem verdadeiros.
# "a or b": Executa se "a" ou "b" forem verdadeiros.
# "not a": Executa se "a" for falso.
# Lembre-se que as parenteses indicam a precedência da operação.
if (num >= 10 and num <= 50) or (num == 99):
    print('O número está no intervalo [10, 50] ou é igual a 99.')

# No python é possível escrever comparações como na matemática regular.
if (10 <= num <= 50) or (num == 99):
    print('O número está no intervalo [10, 50] ou é igual a 99.')

# É possível atribuir valores "booleanos" (Verdadeiro ou falso) para as
# variáveis.
a = True
b = False
c = 2 + 2 == 4  # "c" terá o valor verdadeiro.

```

---

## Estruturas de repetição

```python
# Um loop while executa enquanto a condição for verdadeira, repetindo o
# que estiver no seu bloco de execução.
while True:
    print('Loop infinito!')

# Executa o loop 10 vezes.
a = 0
while a < 10:
    a += 1

# "break" e "continue" alteram o comportamento do loop.
# "break" sai do loop imediatamente.
# "continue" pula para o início do loop imediatamente.
while True:

    user_input = input()

    if user_input == 'saia':
        break  # Sai do loop.
    elif user_input == 'pule a iteração':
        continue  # Vai para o início do loop.

    print('O usuário não saiu, nem pulou a iteração.')

# Um loop "for" executa com base em um intervalo de números ou lista.
# range(início, fim, passo). No exemplo só foi usado um argumento, o fim.
# O intevalo não é inclusivo, o valor 10 não será usado, o loop vai de 0
# até 9.
for i in range(10):
    print(i)

# Caso o índice não seja usado é recomendável deixá-lo como um "_".
for _ in range(10):
    print('Valor não usado.')
```

---

## Listas

```python
# Uma lista é uma coleção de dados indexados.

a = []  # Declaração de uma lista vazia.
b = [1, 2, 3, 4]  # Lista com 4 valores.
c = ['string', 1.5, 4, True]  # Lista com valores de diferentes tipos.

# Para acessar um elemento de uma lista é necessário usar "[índice]".
# Lembrando que a contagem começa em 0.
b[0]  # Acessa o primeiro elemento de uma lista.

# Alguns métodos das listas
b.append(1)     # Adicina o valor "1" no final da lista.
b.insert(1, 5)  # Insere o valor "5" no índice "1" da lista.
b.remove(5)     # Remove o valor "5".
b.sort()        # Ordena a lista.
b.reverse()     # Reverte a lista.
b.count(5)      # Conta quantas vezes o valor "5" aparece na lista.
e = b.copy()    # Copia uma lista para outra.

# Funções aplicáveis nas listas.
len(b)  # Retorna o tamanho de "b".
max(b)  # Retorna o maior valor em "b".
min(b)  # Retorna o menor valor em "b".

# Existem várias outras operações que podem ser feitas.

# Operações extras:
f = a + b  # Une as listas.
g = f[1:4]  # Retorna a lista em um intervalo específico: índice [1, 4).

# É possível checar se um elemento está ou não na lista com o "in".
if 5 in b:
    print('5 está na lista \"b\"')

# Com o "not" é possível verificar se o valor não está na lista.
if 10 not in b:
    print('10 não está na lista \"b\"')

# Outra forma de inicializar as listas é com "List comprehension".
h = [n for n in range(10)]  # Cria uma lista com valores de 0 a 9.
```

---

## Match

```python
# O match é uma feature recente no python (em 2021) e pode ser usado para
# fazer várias comparações sem usar uma cadeia de if's e elif's.

user_input = input()

match user_input:
    case "A":
        print('O input é \"A\"')
    case "B":
        print('O input é \"B\"')
    case _:
        print("O input é outra coisa.")

# Também podem ser usados outros operadores para modificar o comportamento.
match user_input:
    case 'A' | 'C':  # Verifica se é "A" ou "C", ambos são aceitos.
        print('O input é \"A\" ou \"C\"')
    case 'B' | 'D':
        print('O input é \"B\" ou \"D\"')
    case _:
        print('O input é outra coisa.')

```
