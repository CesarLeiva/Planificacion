def prio_ex(list, n):
    procesos_completados = 0
    time = min(int(x.tiempo_llegada) for x in list)
    i = 0
    while procesos_completados < n:
        while i < len(list):
            count = 0
            print(time, list[i].nombre, list[i].tiempo_transcurido, list[i].tiempos, i )
            if int(list[i].tiempo_llegada) <= time and list[i].completed == False:
              
                for j in range(len(list)):
                    if list[i].nombre != list[j].nombre and list[j].completed == False:
                        if list[i].prioridad < list[j].prioridad or list[j].tiempo_llegada > time:
                            count += 1
                            print(count, "count")
                        elif list[i].prioridad > list[j].prioridad and list[j].tiempo_llegada <= time:
                            i+=1
                    else:    
                        count +=1

                if count > 0:
                    list[i].set_tiempo_transcurido(1,time)
                    print(time, "time")
                    time += 1
                    
                    if list[i].tiempo_transcurido == list[i].tiempo_cpu:
                        list[i].completed = True
                        list[i].set_values_ex()
                        procesos_completados += 1 
                        i=0
                        print(procesos_completados, "Procesos", list[i].nombre)
                else:
                    i+=1
            else: 
                i+=1    
            
                
    return list


def prioridad_ex(list, n):
    list = prio_ex(list, n)
    for proceso in list:
        proceso.show_all_info()
        
    
    