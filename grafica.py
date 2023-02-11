from matplotlib import pyplot as plt
import numpy as np
import csv

def graficar_error(error,valor_x):
    fig, ax = plt.subplots()
    ax.set_xlabel('Iteración')
    ax.set_ylabel('Magnitud del error')
    ax.plot(valor_x, error,label='Error')
    ax.legend(loc='upper right')
    plt.savefig('Evolución_error')
    # plt.show()

def graficar_evolucion_pesos(pesos,valor_x):
    list1,list2,list3,list4 = [[],[],[],[]]
    for peso in pesos:
        list1.append(peso[0])
        list2.append(peso[1])
        list3.append(peso[2])
        list4.append(peso[3])
    fig,ax = plt.subplots()
    ax.set_xlabel('Iteración')
    ax.set_ylabel('Evolucion de pesos')
    ax.plot(valor_x, list1, marker='.', label = 'W0')
    ax.plot(valor_x, list2, marker='.', label = 'W1')
    ax.plot(valor_x, list3, marker='.', label = 'W2')
    ax.plot(valor_x, list4, marker='.', label = 'W3')
    ax.legend(loc="upper right")
    plt.savefig('Evolución_pesos')
   
def graficar_versus(y_deseada,y_calculada):
    valor_x = range(1,len(y_deseada)+1)    
    fig, ax = plt.subplots()
    ax.plot(valor_x, y_deseada,color = "green",marker = "x", label="Y Deseada")
    ax.plot(valor_x, y_calculada,color = "red",marker = "o", label="Y Calculada")
    ax.legend(loc="upper right")
    plt.savefig('Comparacion Ys')
    # plt.show()

def graficar_error_versus(error,valor_x):
    identificador = range(1,len(valor_x)+1)
    error_inicial,error_final=[error[0],error[len(error)-1]]
    fig, ax = plt.subplots()
    ax.set_xlabel('ID')
    ax.set_ylabel('Error Observado')
    ax.plot(identificador, error_inicial,label='Error Inicial')
    ax.plot(identificador, error_final,label='Error Final')

    ax.legend(loc='upper right')
    plt.savefig('Error_versus')
    # plt.show()

def reporte(pesos,error_permisible,lista_e_observado, iteraciones):
    # 'Max eObservado',
    titulos=['Pesos iniciales', 'Pesos finales','Error permisible','Error observado','Epocas entrenamiento']
    print(*lista_e_observado,sep='\n')
    with open('reporte.csv', 'w', newline='') as csvfile:
        wr = csv.DictWriter(csvfile, quoting=csv.QUOTE_ALL,fieldnames=titulos)
        # 'Max eObservado':max(lista_e_observado),
        dic_print=[{'Pesos iniciales':pesos[0],'Pesos finales':pesos[len(pesos)-1],'Error permisible':error_permisible,'Error observado':lista_e_observado[len(lista_e_observado)-1],'Epocas entrenamiento':iteraciones}]
        wr.writeheader()
        wr.writerows(dic_print)
