
def fifo(list):
    lista_ordenada = sorted(list, key=lambda x: x.tiempo_llegada)
    time = 0
    for proceso in lista_ordenada:
        tiempo_comienzo = time
        tiempo_fin = time + proceso.tiempo_cpu
        time = tiempo_fin
        proceso.set_values(tiempo_comienzo, tiempo_fin)
    