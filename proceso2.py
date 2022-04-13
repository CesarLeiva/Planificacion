# Crear objeto proceso con los siguientes atributos, nombre o ID y  valores de tiempo.
import random
class Proceso2:
    def __init__(self, nombre, tiempo_llegada, tiempo_cpu, prioridad):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_cpu = tiempo_cpu
        self.prioridad = prioridad 
        self.completed = False
        self.tiempo_transcurido = 0
    
    def show_basic_info(self):
        print(f"\nProceso con nombre: {self.nombre}")
        print(f"\ntiempo de llegada: {self.tiempo_llegada}")
        print(f"tiempo de cpu: {self.tiempo_cpu}")
        print(f"tiempo de prioridad: {self.prioridad}")
    
    def set_values(self, tiempo_comienzo, tiempo_fin ):
        self.tiempo_comienzo = tiempo_comienzo
        self.tiempo_fin = tiempo_fin
        self.tiempo_espera =  self.tiempo_comienzo - self.tiempo_llegada
    
    def set_values_ex(self):
        lista_tiempo = self.tiempos
        for i in range(len(lista_tiempo)):
            if lista_tiempo[i] + 1 == lista_tiempo[i+1]
            
       
      
    def set_tiempo_transcurido(self, tiempo_transcurido):
        self.tiempo_transcurido  += tiempo_transcurido
        self.tiempos.append(tiempo_transcurido)
        

    def show_all_info(self):
        print(f"\nProceso con nombre: {self.nombre}")
        print(f"\ntiempo de llegada: {self.tiempo_llegada}")
        print(f"tiempo de cpu: {self.tiempo_cpu}")
        print(f"tiempo de prioridad: {self.prioridad}")
        print(f"tiempo de comienzo: {self.tiempo_comienzo}")
        print(f"tiempo de fin: {self.tiempo_fin}")

