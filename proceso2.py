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
        self.tiempos = []
    
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
        lista_tiempo_final = self.tiempos.copy()
        lista_tiempo_comienzo = self.tiempos.copy()
        tamaño_lista = len(self.tiempos)
        for i in range(tamaño_lista - 1):
             if self.tiempos[i] + 1  == self.tiempos[i + 1]:
                 lista_tiempo_final.pop(i)

        for i in reversed(range(tamaño_lista)): 
            if self.tiempos[i] == self.tiempos[i-1] + 1:
                lista_tiempo_comienzo.pop(i)

        self.tiempo_comienzo = lista_tiempo_comienzo
        self.tiempo_fin = lista_tiempo_final
            
      
    def set_tiempo_transcurido(self, tiempo_transcurido, linea_tiempo):
        self.tiempo_transcurido  += tiempo_transcurido
        self.tiempos.append(linea_tiempo)
        

    def show_all_info(self):
        print(f"\nProceso con nombre: {self.nombre}")
        print(f"\ntiempo de llegada: {self.tiempo_llegada}")
        print(f"tiempo de cpu: {self.tiempo_cpu}")
        print(f"tiempo de prioridad: {self.prioridad}")
        print(f"tiempo de comienzo: {self.tiempo_comienzo}")
        print(f"tiempo de fin: {self.tiempo_fin}")

