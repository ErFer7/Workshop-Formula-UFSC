# -*- coding: utf-8 -*-

'''
Converte o tempo de segundos para HH:MM:SS
'''

seconds = int(input("Digite o tempo em segundos: "))

minutes = seconds / 60
hours = minutes / 60

minutes %= 60
seconds %= 60

seconds = int(seconds)
minutes = int(minutes)
hours = int(hours)

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
