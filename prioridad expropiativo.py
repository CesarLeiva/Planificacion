def prio_ex(list, n):
    procesos_completados = 0
    time = min(int(x.tiempo_llegada) for x in list)
    while procesos_completados < n:
        for i in range(len(list)):
            count = 0
            if int(list[i].tiempo_llegada) <= time and list[i].completed == False:
                for j in range(len(list)):
                    if list[i].prioridad >= list[j].prioridad and list[j].completed == False and int(list[j].tiempo_llegada) <= time and list[i].tiempo_cpu != list[j].tiempo_cpu:
                        list[i], list[j] = list[j], list[i]
                        count+= 1
                        print(count, "count", j , i)
                        break
                
                if count == 0:
                    tiempo_comienzo = time
                    list[i].set_tiempo_transcurido(time)
                    time += 1
                    
                    if list[i].tiempo_transcurido == list[i].tiempo_cpu:
                        list[i].completed = True
                        list[i].set_values_ex()
                        procesos_completados += 1 
                        print(procesos_completados)

                else:
                    break
    return list


def prioridad_al(list, n):
    list = prio_ex(list, n)
    for proceso in list:
        proceso.show_all_info()
        
    
    