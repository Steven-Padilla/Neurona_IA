import random
import numpy
from interfaz import Interfaz
from grafica import graficar_error
class Neurona():
    def __init__(self, eta, cantidad_x,error_permisible):
        self.eta = eta
        self.cantidad_x = cantidad_x
        self.error_permisible = error_permisible
        self.lista_x = numpy.array([[651.92, 645.61, -990.08],
                        [-804.69, 333.05, 682.68],
                        [-220.11, -333.26, 780.61],
                        [-337.46, 616.51, -864.44],
                        [257.56, 507.27, -774.94]])
        self.y_deseada = numpy.array([-6914.52, 1783.1, 4052, -4545.16, -4937.24])
        self.lista_w = self.generar_w()
        self.lista_e=[]
        self.lista_iter = []
        aux = 1
        self.err_viejo=1
        self.err_nuevo=0
        while self.err_nuevo > self.error_permisible and self.err_viejo > self.err_nuevo:
            self.lista_u = self.calcular_u()
            self.y_calculada=self.funcion_activacion()
            self.error = self.calcular_error()
            self.lista_w=self.nueva_w()
            self.lista_iter.append(aux+1)
            aux += 1
        graficar_error(self.lista_e,self.lista_iter)

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
        e = numpy.subtract(self.y_deseada, self.y_calculada)
        self.err_viejo=self.err_nuevo
        self.err_nuevo=numpy.linalg.norm(e)
        self.lista_e.append(self.err_nuevo)
        return e

    def nueva_w(self):
        multi = numpy.matmul(numpy.transpose(self.error), self.lista_x)
        aprendizaje = numpy.dot(self.eta,multi) 
        nueva_w = self.lista_w+aprendizaje
        print(f'Lista u: {self.lista_u}')
        return nueva_w



if __name__ == '__main__':
    data=Interfaz().get_datos()

    algotirmo = Neurona(eta=data['aprendizaje'], cantidad_x=3,error_permisible=data['margen_error'])
