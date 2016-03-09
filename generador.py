"""
Un generador de senal es el responsable de generar una senal portadora.

"""
import matplotlib.pyplot as plt

class Generador(object):

    def __init__(self, amplitud, fase, frecuencia):
        self.amplitud = amplitud
        self.fase = fase
        self.frecuencia = frecuencia

        #  muestras por segundo
        self.frecuencia_muestreo = frecuencia*3


    def generar(self, tiempo_inicial, tiempo_final):

        import math

        cantidad_muestras = (tiempo_final - tiempo_inicial).seconds/\
        self.frecuencia_muestreo
        cantidad_muestras = int(cantidad_muestras) #tuve que agregar esta linea
        muestras = range(cantidad_muestras)
        #TODO agregar un ruido blanco a la senal

        ret = [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
        for i in muestras]
        plt.plot(ret)
        return ret
