from matplotlib import pyplot as plt
def graficar_error(error,valor_x):
    fig, ax = plt.subplots()
    ax.set_xlabel('Iteración')
    ax.set_ylabel('Magnitud del error')
    ax.plot(valor_x, error,label='Error')
    ax.legend(loc='upper right')
    plt.show()

