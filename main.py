# Desarrollar un simulador de planificador de procesos que cumpla con los siguientes requerimientos:
# • Capture el numero de procesos para las respectivas simulaciones con la siguiente
# restricción: Mínimo 4 procesos, Máximo 8
# • Permita asignar al usuario los valores de tiempos de llegada, CPU y nombres o ID de los
# procesos
# • Calcule y genere tablas con los datos exactos de la simulación. Tiempos de comienzo, final
# y espera 
# • Ofrecer un menú al usuario que le permita escoger el algoritmo con el que desea hacer la
# simulación. (FIFO, SJF, PRIORIDAD (EXP-NO EXP), SRTF)


# Algoritmo de planificacion de procesos 
# Luis Sebastian Olivares Puello - 0221910015
# Daniel
# Cesar
from proceso import *
from fifo import *
from sjf import *
from prioridad import *                
                
def main():
    number_processes = int(input("\nDigitar el numero de procesos que interacturan(Min 4 - Max 8): "))

    list_procesos = []

    # Creacion de los objetos de la clase Proceso
    for iterador in range(number_processes):
        print(f"\nProceso numero {iterador+1}")
        nombre = str(input("Digite el nombre del proceso: "))
        tiempo_llegada = int(input("Digite el tiempo de llegada del proceso: "))
        tiempo_cpu = int(input("Digite el tiempo en cpu del proceso: "))
        prioridad = int(input("Digite la prioridad del proceso: "))
        list_procesos.append(Proceso(nombre,tiempo_llegada,tiempo_cpu,prioridad))


    fifo(list_procesos)
    # sjf(list_procesos, number_processes)
    # prioridad_al(list_procesos, number_processes)



if __name__ == "__main__":
    main()