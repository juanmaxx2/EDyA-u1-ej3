import numpy as np

class Pila:
    __cant = 0 
    __tope = -1

    def __init__(self, cant):
        self.__item = np.empty(cant, dtype = int)
        self.__tope = -1
        self.__cant = cant

    def vacio(self):
        return (self.__tope == -1)

    def insertar(self, x):
        if (self.__tope < self.__cant-1):
            self.__tope += 1
            self.__item[self.__tope] = x
            return x
        else: print("\nLa pila esta llena")

    def suprimir (self):
        if (self.vacio()):
            print("\nLa pila esta vacia")
        else:
            self.__item = np.delete(self.__item,self.__tope)
            self.__tope -= 1

    def mostrar (self):
        if not (self.vacio()):
            i = self.__tope
            while (i >= 0):
                if i == self.__tope:
                    print(self.__item[i])
                else:
                    print('x')
                    print(self.__item[i])
                i -= 1