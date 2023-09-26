class Matriz():
    def __init__(self, elemento, ):
        self.elemento = elemento


class traspuesta(Matriz):
    def __init__(self, elemento, ):
        super().__init__(elemento)

    def calcular_traspuesta(self):
        traspuesta = []
        for i in range(len(self.elemento[0])):
            fila = []
            traspuesta.append([])
            for j in range(len(self.elemento)):
                traspuesta[i].append(self.elemento[j][i])
            traspuesta.append(fila)
        return Imprimir(traspuesta)
    
class Imprimir(Matriz):
    def __init__(self, elemento, ):
        super().__init__(elemento)

    def imprimir_traspuesta(self):
        for fila in self.elemento:
            print(fila)
class lanzador(Imprimir, traspuesta):
    def __init__(self, ):
        self.elemento = []
        self.cantidad_filas = int(input("Ingrese la cantidad de filas: "))
        self.cantidad_columnas = int(input("Ingrese la cantidad de columnas: "))
        self.crear_matriz()
        self.matriz = Matriz(self.elemento)
        self.traspuesta = traspuesta(self.elemento)
        self.imprimir = Imprimir(self.elemento)
        super().__init__(self.elemento)

    def crear_matriz(self):
        for i in range(self.cantidad_filas):
            fila = []
            self.elemento.append([])
            for j in range(self.cantidad_columnas):
                self.elemento[i].append(int(input(f"Elemento {i},{j}: ")))
            self.elemento.append(fila)
    
    def lanzar(self ):
        print("Matriz es: ")
        self.imprimir.imprimir()
        print("Traspuesta es :")
        traspuesta_result= self.traspuesta.calcular_traspuesta()
        imprimir_traspuesta = Imprimir(traspuesta_result)
        self.traspuesta().imprimir()
        
        
if __name__ == "__main__":
    lanzador = lanzador()
    lanzador.lanzar()
        