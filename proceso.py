# Crear objeto proceso con los siguientes atributos, nombre o ID y  valores de tiempo.
import random
class Proceso:
    def __init__(self, nombre, tiempo_llegada, tiempo_cpu, prioridad):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_cpu = tiempo_cpu
        self.prioridad = prioridad 
        self.completed = False
    
    def show_basic_info(self):
        print(f"\nProceso con nombre: {self.nombre}")
        print(f"\ntiempo de llegada: {self.tiempo_llegada}")
        print(f"tiempo de cpu: {self.tiempo_cpu}")
        print(f"tiempo de prioridad: {self.prioridad}")
    
    def set_values(self, tiempo_comienzo, tiempo_fin ):
        self.tiempo_comienzo = tiempo_comienzo
        self.tiempo_fin = tiempo_fin
        self.tiempo_espera =  self.tiempo_comienzo - self.tiempo_llegada
        
    def show_all_info(self):
        print(f"\nProceso con nombre: {self.nombre}")
        print(f"\ntiempo de llegada: {self.tiempo_llegada}")
        print(f"tiempo de cpu: {self.tiempo_cpu}")
        print(f"tiempo de prioridad: {self.prioridad}")
        print(f"tiempo de comienzo: {self.tiempo_comienzo}")
        print(f"tiempo de fin: {self.tiempo_fin}")
        print(f"tiempo de espera: {self.tiempo_espera}")

