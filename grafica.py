from matplotlib import pyplot as plt
import numpy as np
import csv

def graficar_error(error,valor_x):
    fig, ax = plt.subplots()
    ax.set_xlabel('Iteración')
    ax.set_ylabel('Magnitud del error')
    ax.plot(valor_x, error,label='Error')
    ax.legend(loc='upper right')
    plt.show()

def graficar_evolucion_pesos(pesos,valor_x):
    list1,list2,list3,list4 = [[],[],[],[]]
    for peso in pesos:
        list1.append(peso[0])
        list2.append(peso[1])
        list3.append(peso[2])
        list4.append(peso[3])

        
    print(f'peso: {pesos}')
    fig,ax = plt.subplots()
    ax.set_xlabel('Iteración')
    ax.set_ylabel('Evolucion de pesos')
    ax.plot(valor_x, list1, marker='.', label = 'W SESGO')
    ax.plot(valor_x, list2, marker='.', label = 'W X1')
    ax.plot(valor_x, list3, marker='.', label = 'W X2')
    ax.plot(valor_x, list4, marker='.', label = 'W X3')
    ax.legend(loc="upper right")
    plt.show()
def graficar_versus(y_deseada,y_calculada):
    valor_x = range(1,len(y_deseada)+1)
    n=0
    print(f'y deseada: {y_deseada}')
    print(f'y calulada: {y_calculada}')
    
    fig, ax = plt.subplots()
    ax.plot(valor_x, y_deseada,color = "green",marker = "x", label="Y Deseada")
    ax.plot(valor_x, y_calculada,color = "red",marker = "o", label="Y Calculada")
    ax.legend(loc="upper right")
    plt.show()

def graficar_error_versus(error,valor_x):
    identificador = range(1,len(valor_x)+1)
    error_inicial,error_final=[error[0],error[len(error)-1]]
    print(f'error: {error_final}')
    fig, ax = plt.subplots()
    ax.set_xlabel('ID')
    ax.set_ylabel('Error Observado')
    ax.plot(identificador, error_inicial,label='Error Inicial')
    ax.plot(identificador, error_final,label='Error Final')

    ax.legend(loc='upper right')
    plt.show()

def reporte():
    pass
