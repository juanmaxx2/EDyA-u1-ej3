class Pila:
    __Tope = None
    __Elemento = None

    def __init__(self):
        self.__Tope = -1
        self.__Elemento = []
    
    def Vacio(self):
        return (self.__Tope == -1)

    def Insertar(self, x):
        self.__Tope += 1
        self.__Elemento.append(x)
        return x
    
    def Suprimir(self):
        if (self.Vacio()):
            print("\nLa pila esta vacia")
            return 0
        else:
            self.__Tope -= 1
            x = self.__Elemento.pop(self.__Tope)
            return x
        
    def Mostrar(self):
        if not(self.Vacio()):
            i = self.__Tope
            while(i>=0):
                print(self.__Elemento[i])
                i-=1