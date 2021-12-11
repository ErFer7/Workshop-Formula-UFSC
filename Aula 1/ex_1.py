# -*- coding: utf-8 -*-

'''
Converte o tempo de HH:MM:SS para segundos.
'''

hours, minutes, seconds = map(int, input("Digite o tempo: ").split(':'))

total_time = hours * 3600
total_time += minutes * 60
total_time += seconds

print(f"{total_time} segundo(s)")
