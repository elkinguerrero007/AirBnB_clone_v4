#!/usr/bin/python3
# Recibir 3 datos correspondientes a:
# Distancia(mts), velocidad permitida (km/h) y tiempo transccurrido(sec)
distancia, vel_max, tiempo = input().split()
distancia = float(distancia)
vel_max, tiempo = int(vel_max), int(tiempo)
# Calcular la velocidad capturada (v = d/t)
# Convertir la velocidad de m/s a km/h (km/h = (m/s) * (3600/1000))
vel_real = (distancia / tiempo) * 3.6
# Mostrar el mensaje según el caso.
if distancia < 0 or vel_max < 0 or tiempo < 0:
    print("ERROR")
elif vel_real < vel_max:
    print("OK")
else:
    if (vel_real - vel_max) < (vel_max * 0.20):
        print("MULTA")
    else:
        print("CURSO SENSIBILIZACION")
