class Blanco(object):
    """
    Define un blanco a ser detectado por un radar
    """

    def __init__(self, amplitud, tiempo_inicial, tiempo_final):
        self.amplitud = amplitud
        self.tiempo_inicial = tiempo_inicial
        self.tiempo_final = tiempo_final
    
    def reflejar(self, senal, tiempo_inicial, tiempo_final):
        
        #busco el intervalo de tiempo
        if tiempo_inicial>self.tiempo_final:
            pass
        
        if tiempo_inicial<self.tiempo_inicial:
            comienzo = self.tiempo_inicial
        else:
            comienzo = tiempo_inicial
            
        if tiempo_final<self.tiempo_inicial:
            pass
        if tiempo_final<self.tiempo_final:
            final = tiempo_final
        else:
            final = self.tiempo_final
        
        
        ret =  senal[comienzo:final] =  \
        [self.amplitud*math.sin(2*(1/self.frecuencia)*i+self.fase) \
        for i in muestras]
        
        #TODO ver como se encajan los tiempos del blanco y del intervalo de tiempo
        #(interseccion de invervalos)
        # despues aplicar los parametros del blanco sobre ese intervalo de tiempo
        pass
        
