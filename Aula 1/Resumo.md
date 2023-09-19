# Resumo - Aula 1

## Exibição de output

---

```python
print('Hello World!')
```

## Operações básicas

---

```python
2 + 2   # Adição
2 - 2   # Subtração
2 * 2   # Multiplicação
2 / 2   # Divisão (Retorna um float!)
2 // 2  # Quociente
2 % 2   # Resto
2 ** 2  # Exponenciação
```

## Variáveis

---

```python
a = 0  # Declaração de uma variável com o valor '0'

# O python possui regras de nomenclatura. Os nomes das variáveis devem
# começar com letras, símbolos e números não são permitidos. Além disso,
# a linguagem tem recomendações quanto a formatação. Procure pela 'PEP 8'
# para saber mais sobre a formatação do python.
snake_case = 'Veja a PEP 8'

# Os valores nas variáveis possuem tipos diferentes. Aqui estão alguns
# exemplos:
a = 1        # Tipo 'int'
b = 1.25     # Tipo 'float'
c = 'texto'  # Tipo 'str' ou string
d = True     # Tipo 'bool'
```

### Operações com variáveis

```python
a, b = 1, 2

c = a + b   # Adição
d = a - b   # Subtração
e = a * b   # Multiplicação
f = a / b   # Divisão
g = a // b  # Quociente
h = a % b   # Resto
i = a ** b  # Exponenciação

# Caso a operação seja em cima de uma única variável, é possível resumir a
# sintaxe.
a += 1  # Equivalente à 'a = a + 1'

# Outros casos
a -= 2   # Equivalente à 'a = a - 2'
a *= 2   # Equivalente à 'a = a * 2'
a /= 2   # Equivalente à 'a = a / 2'
a //= 2  # Equivalente à 'a = a // 2'
a %= 2   # Equivalente à 'a = a % 2'
a **= 2  # Equivalente à 'a = a ** 2'
```

## Output com formatação

---

```python
a = 2.55

# Formatações para exibir 'a = 2.55' com a precisão de duas casas decimais

print('a = %.2f' % a)           # Estilo C
print('a = {0:.2f}'.format(a))  # Format
print(f'a = {a:.2f}')           # f-string

# É possível utilizar esta formatação também (não garante a precisão de
# duas casas).
print('a = ', a)
```
