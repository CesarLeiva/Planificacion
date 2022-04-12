from operator import itemgetter, attrgetter

def bubblesort(list):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(list) - 1):
            if list[i].tiempo_cpu > list[i+1].tiempo_cpu:
                list[i], list[i+1] = list[i+1], list[i]
                intercambio = True
    return list


def bubblesort2(list):
    intercambio = True
    while intercambio:
        time = min(int(x.tiempo_llegada) for x in list)
        intercambio = False
        for i in range(len(list) - 1):
            list[i].completed = True
            print(time)
            count = 0
            if int(list[i].tiempo_llegada) <= time:
                for j in range(len(list) - 1):
                    if list[i].tiempo_cpu > list[j].tiempo_cpu and list[j].completed == False:
                        list[i], list[i+1] = list[i+1], list[i]
                        intercambio = True
                        count+= 1
                if count >= 1:
                    list[i].completed = True
                    time = time + list[i].tiempo_cpu
            else:
                list[i], list[i+1] = list[i+1], list[i]
                intercambio = True
                
    return list

def tiempo_llegada(list, n):
    procesos_completados = 0
    time = min(int(x.tiempo_llegada) for x in list)
    while procesos_completados < n:
        for i in range(len(list)):
            count = 0
            if int(list[i].tiempo_llegada) <= time and list[i].completed == False:
                for j in range(len(list)):
                    if list[i].tiempo_cpu >= list[j].tiempo_cpu and list[j].completed == False and int(list[j].tiempo_llegada) <= time and list[i].tiempo_cpu != list[j].tiempo_cpu:
                        list[i], list[j] = list[j], list[i]
                        count+= 1
                        print(count, "count", j , i)
                        break
                
                if count == 0:
                    tiempo_comienzo = time
                    time = time + list[i].tiempo_cpu
                    list[i].completed = True
                    procesos_completados += 1 
                    print(procesos_completados)
                    list[i].set_values(tiempo_comienzo, time)
                else:
                    break
    return list


def sjf(list, n):
    list = tiempo_llegada(list, n)
    for proceso in list:
        proceso.show_all_info()
        
    
    
