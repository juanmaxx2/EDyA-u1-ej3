from pila import Pila
if __name__ == "__main__":
    x = int(input("\nIngrese el numero que desea conseguir el factorial:"))
    unaPila = Pila(x)
    elem = x
    for i in range(elem):
        unaPila.insertar(elem)
        elem -= 1
    print("\nEl factorial de un numero es:")
    unaPila.mostrar()