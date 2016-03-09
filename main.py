#!/usr/bin/env python

import radar
import medio
import blanco
import generador
import datetime
import detector
import math
import matplotlib.pyplot as plt

# DISCLAMER!!
# todo esta en castellano por razones didacticas
# pero DEBEN programar en INGLES
# uno nunca sabe quien puede leer su codigo

def main():

    # Intervalo de tiempo en el que vamos a medir
    tiempo_inicial = datetime.datetime(2016, 3, 5, 1)
    tiempo_final = datetime.datetime(2016, 3, 5, 10)


    # parametros del generador de senales
    amplitud = 0.2
    fase = 1
    frecuencia = 20*math.pi

    #TODO construir un nuevo genrador de senales    
    generador_creado = generador.Generador(amplitud, fase, frecuencia)    
    #print generador_creado
    generador_creado.generar(tiempo_inicial,tiempo_final)
    #TODO construir un detector
    detector_creado = detector.Detector()

    #TODO construir un nuevo radar
    radar_creado = radar.Radar(generador_creado, detector_creado)
    #print radar_creado
    
    # parametros para un blanco
    amplitud_de_frecuencia_del_blanco = amplitud + 100
    tiempo_inicial_del_blanco = datetime.datetime(2016, 3, 5, 2)
    tiempo_final_del_blanco = datetime.datetime(2016, 3, 5, 4)
    
    #TODO contruir un nuevo blanco
    blanco_creado = blanco.Blanco(amplitud_de_frecuencia_del_blanco, tiempo_inicial_del_blanco, tiempo_final_del_blanco)
#    print blanco_creado.amplitud

    #TODO contruir un medio
    medio_creado = medio.Medio(blanco)
    
    #usar radar
    encontro = radar_creado.detectar(medio_creado, tiempo_inicial, tiempo_final)
    
    
if __name__ == "__main__":
    main()
