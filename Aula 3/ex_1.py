# -*- coding: utf-8 -*-

'''
Para resolver o problema é necessário considerar todas as posições da matriz primeiro. Para isso são
usadas duas funções de tranformação de matrizes, a função de rotação e uma de espelhamento.

O programa compara cada elemento em cada matriz com a função "comp_mat" que retorna a precisão.

A matriz que está sendo testada é rotacionada para os quatro possíveis lados e para cada rotação é comparada
novamente com a matriz padrão. Depois disso ela é espelhada e rotacionada para os quatro possíveis lados e
comparada também.

As precisões ficam registradas em uma lista que no fim exibe o valor máximo.
'''

# A função "flip" espelha a matriz. Nesta função cada linha é revertida e colocada em uma matriz
# que será retornada
def flip(mat, lenght):
    '''
    Espelha a matriz.
    '''

    flipped_mat = [] # Matriz para retorno

    # Inverte cada linha da matriz e coloca na matriz de retorno
    for i in range(lenght):

        flipped_mat.append(list(reversed(mat[i])))

    return flipped_mat # Retorna a matriz espelhada

# Esta função rotaciona a matriz no sentido horário. Ela é uma função recursiva, então o valor de "a" define
# Quantas vezes será feita uma rotação. Ex: a = 2 -> rotaciona duas vezes, deixando a matriz de ponta-cabeça.
def rot(mat, lenght, angle = 1):
    '''
    Rotaciona a matriz.
    '''

    # Caso nenhuma rotação seja especificada retorna a própria matriz
    if angle == 0:

        return mat

    rotated_mat = [] # Matriz para retorno

    # Adiciona cada coluna da matriz original em linhas da nova matriz. O primeiro elemento da nova linha
    # será o último elemento da coluna
    for i in range(lenght):

        rotated_mat.append([])

        for j in range(lenght):

            rotated_mat[i].append(mat[lenght - j - 1][i])

    angle -= 1 # Decrementa o a

    if angle <= 0: # Caso as rotações terminaram

        return rotated_mat # Retorna a nova matriz
    else: # Caso contrário

        return rot(rotated_mat, lenght, angle) # Chama a função recursivamente para mais uma rotação

# Esta função compara a diferença de cada elemento e calcula a precisão entre as matrizes
def comp_mat(mat_a, mat_b, lenght):

    p_count = 0 # Variável para a quantidade de elementos que satisfazem os critérios

    # Para cada elemento verifica se a diferença entre eles é menor ou igual a 100
    # Caso seja incrementa a quantidade de elementos precisos.
    for i in range(lenght):

        for j in range(lenght):

            if abs(mat_a[i][j] - mat_b[i][j]) <= 100:

                p_count += 1

    return (p_count * 100.0) / lenght ** 2.0 # Retorna o valor percentual da precisão

while True: # Loop para cada caso

    l = int(input()) # Entrada de l

    # Condição de saída
    if l == 0:
        break

    p_mat = [] # Matriz padrão
    t_mat = [] # Matriz de testes

    # Loop para a entrada da matriz padrão
    for _ in range(l):

        lst = list(map(int, input().split()))
        p_mat.append(lst)

    # Loop para a entrada da matriz de testes
    for _ in range(l):

        lst = list(map(int, input().split()))
        t_mat.append(lst)

    p_lst = [] # Lista de precisões

    for a in range(4): # Loop para cada rotação

        rot_mat = rot(t_mat, l, a) # Matriz rotacionada

        p_lst.append(comp_mat(p_mat, rot_mat, l)) # Adiciona a precisão na lista de precisões

    flip_mat = flip(t_mat, l) # Matriz espelhada

    for a in range(4): # Loop para cada rotação espelhada

        rot_mat = rot(flip_mat, l, a) # Matriz espelhada rotacionada

        p_lst.append(comp_mat(p_mat, rot_mat, l)) # Adiciona a precisão na lista de precisões

    print(f"{max(p_lst):.2f}") # Exibe o resultado
