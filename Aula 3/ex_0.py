# -*- coding: utf-8 -*-

'''
Aula 2.

Este programa conta a quantidade de cada palavra e um texto.

Esta não é necessariamente a forma mais ideal, aqui os dicionários foram usados como um exemplo apenas.
'''

text = input().split()

for i, word in enumerate(text):
    text[i] = word.lower()

count_dict = {}

for word in text:

    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

for key in count_dict:
    print(f"A palavra \"{key}\" foi encontrada {count_dict[key]} vezes no texto")
