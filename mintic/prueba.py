#!/usr/bin/python3

n = int(input())

eje_pedalier, biela, sillin, manillar, valor = input().split()

eje_pedalier = int(eje_pedalier)
biela = int(biela)
sillin = int(sillin)
manillar = int(manillar)
valor = int(valor)
lista = []

lista.append(eje_pedalier)

print(lista)


if(eje_pedalier > 239 and eje_pedalier < 301 and biela > 179 and biela < 161 and sillin > 239 and sillin < 276 and manillar < 51 and valor < 1195):
    print(eje_pedalier)
    
