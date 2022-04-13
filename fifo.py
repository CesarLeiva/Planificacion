
def bubblesort(list):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(list) - 1):
            if list[i].tiempo_llegada > list[i+1].tiempo_llegada:
                list[i], list[i+1] = list[i+1], list[i]
                intercambio = True
    return list

def fifo(list):
    # lista_ordenada = sorted(list, key=lambda x: x.tiempo_llegada)
    lista_ordenada = bubblesort(list)
    time = 0
    for proceso in lista_ordenada:
        tiempo_comienzo = time
        tiempo_fin = time + proceso.tiempo_cpu
        time = tiempo_fin
        proceso.set_values(tiempo_comienzo, tiempo_fin)
        proceso.show_all_info()

    