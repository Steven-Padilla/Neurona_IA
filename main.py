import random
import numpy
import csv
import pandas as pd
from interfaz import Interfaz
from grafica import graficar_error, graficar_evolucion_pesos, graficar_versus, graficar_error_versus
class Neurona():
    def __init__(self, eta, cantidad_x,error_permisible):
        self.eta = eta
        self.cantidad_x = cantidad_x
        self.error_permisible = error_permisible
        self.lista_x, self.y_deseada =self.leer_csv() 
        self.lista_w = self.generar_w()
        self.lista_pesos = []
        self.lista_e=[]
        self.lista_iter = []
        self.lista_error_observado = []
        self.aux = 1
        self.err_viejo=0
        self.err_nuevo=0
        self.iniciar_alg()
        
        while self.err_nuevo > self.error_permisible :
            if self.err_viejo ==0  :
                self.iniciar_alg()
            elif self.err_viejo > self.err_nuevo:
                self.iniciar_alg()
            else:
                break
            

        graficar_error(self.lista_e,self.lista_iter)
        graficar_evolucion_pesos(self.lista_pesos,self.lista_iter)
        graficar_versus(self.y_deseada, self.y_calculada)
        graficar_error_versus(self.lista_error_observado,self.y_deseada)

    def iniciar_alg(self):
        self.lista_u = self.calcular_u()
        self.y_calculada=self.funcion_activacion()
        self.error = self.calcular_error()
        self.lista_w=self.nueva_w()
        self.lista_iter.append(self.aux)
        self.aux += 1
        
    def generar_w(self):
        lista_w = []
        while len(lista_w) < self.cantidad_x:
            lista_w.append(round(random.uniform(-1, 1), 2))
        print(f'Lista de pesos: {lista_w}')
        return lista_w

    def calcular_u(self):
        lista_u = numpy.matmul(self.lista_x, numpy.transpose(self.lista_w))
        # print(f'Lista u: {lista_u}')
        return lista_u

    def funcion_activacion(self):
        return self.lista_u

    def calcular_error(self):
        e = numpy.subtract(self.y_deseada,self.y_calculada)
        self.err_viejo=self.err_nuevo #0
        print(f'error viejo: {self.err_viejo}')
        self.lista_error_observado.append(e)
        self.err_nuevo=numpy.linalg.norm(e)  #error random
        print(f'error nuevo: {self.err_nuevo}')
        self.lista_e.append(self.err_nuevo)
        return e

    def nueva_w(self):
        e_x = numpy.matmul(numpy.transpose(self.error), self.lista_x)
        n_ex = numpy.dot(self.eta,e_x) 
        nueva_w = self.lista_w+n_ex
        self.lista_pesos.append(nueva_w)
        # print(f'Lista u: {self.lista_u}')
        return nueva_w

    def leer_csv(self):
        data = pd.read_csv('203404_prueba.csv')
        sesgo=self.calcular_sesgo(data)
        sesgo=pd.DataFrame(data=sesgo)
        lista_x=pd.concat([sesgo,data[['X1','X2','X3']]],axis=1).values.tolist()
        lista_y=data[['Y']].values.tolist()
        arr_aux=[]
        for y in lista_y:
            arr_aux.append(y[0])
        return (numpy.array(lista_x), numpy.array(arr_aux))
    def calcular_sesgo(self,data):
        sesgo=[1 for _ in range(len(data.axes[0]))]
        print(len(sesgo))
        return sesgo

if __name__ == '__main__':
    data=Interfaz().get_datos()

    algotirmo = Neurona(eta=data['aprendizaje'], cantidad_x=4,error_permisible=data['margen_error'])
