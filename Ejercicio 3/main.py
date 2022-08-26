from pila import Pila
if __name__ == "__main__":
    unaPila = Pila()
    x = int(input('Ingrese el numero que desea factorizar:'))
    NumerosPrimos = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    aux = x
    i=0
    while (x > 1):
        if ((x%NumerosPrimos[i]) == 0):
            x = x/NumerosPrimos[i]
            unaPila.Insertar(NumerosPrimos[i])
        else:
            i += 1
    unaPila.Mostrar()