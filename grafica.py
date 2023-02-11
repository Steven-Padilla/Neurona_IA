from matplotlib import pyplot as plt
import numpy as np

def graficar_error(error,valor_x):
    fig, ax = plt.subplots()
    ax.set_xlabel('Iteración')
    ax.set_ylabel('Magnitud del error')
    ax.plot(valor_x, error,label='Error')
    ax.legend(loc='upper right')
    plt.show()

def graficar_evolucion_pesos(pesos,valor_x):
    n = 0
    resim_data = np.asarray(pesos)
    resim_data = resim_data[:,n,:]

    fig,ax = plt.subplots()
    ax.set_xlabel('Iteración')
    ax.set_ylabel('Evolucion de pesos')
    ax.plot(valor_x, resim_data, marker='.')

    plt.show()
def graficar_versus(y_deseada,y_calculada,valor_x):
    n=0
    resim_y_deseada = np.asarray(y_deseada)
    resim_y_calculada = np.asarray(y_calculada)
    resim_y_deseada = resim_y_deseada[:,n]
    resim_y_calculada = resim_y_calculada[:,n]

    print(f'y deseada: {resim_y_deseada}')
    print(f'y calulada: {resim_y_calculada}')
    
    fig, ax = plt.subplots()
    ax.plot(valor_x, resim_y_deseada, label="Y Deseada")
    ax.plot(valor_x, resim_y_calculada, label="Y Calculada")
    ax.legend(loc="upper right")
    plt.show()

