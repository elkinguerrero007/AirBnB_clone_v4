#!/usr/bin/python3
salario_base, num_horas_extras, bono = input().split()
salario_base = int(salario_base)
num_horas_extras = int(num_horas_extras)
bono = int(bono)

bonificacion = 0
hora_base = salario_base / 192
hora_extra = hora_base * 1.25
pago_hora_extra = num_horas_extras * hora_extra

if(bono == 1):
    bonificacion = salario_base * 0.05

salario_total = salario_base + pago_hora_extra + bonificacion
salud = salario_total * 0.035
pension = salario_total * 0.04
compensacion = salario_total * 0.01
aportes = pension + salud + compensacion
liquidacion = salario_total - aportes

print("{:.1f}".format(liquidacion))