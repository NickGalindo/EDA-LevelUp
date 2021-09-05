'''
Implementación de una cola prioritaria en python con estructuras propias
'''
#i es la posicion en el arreglo
#los valores en el arreglo son arreglos [volumen][nombreusuario]
class MaxHeap:

    def __init__(self, max_size):
        self.H = [None]*max_size
        self.size = 0
        self.max_size = max_size

    def parent(self, i):
        'Devuelve el padre del elemento i'
        return (i-1)//2

    def left_child(self, i):
        'Devuelve el hijo izquierdo'
        return 2*i + 1

    def right_child(self, i):
        'Devuelve el hijo derecho'
        return 2*i + 2

    def swap(self, first, second):
        'Intercambia los valores de dos indices'
        tmp = self.H[first]
        self.H[first] = self.H[second]
        self.H[second] = tmp
        return

    def sift_up(self, i):
        'Filtrar hacia arriba, ordenar un elemento con respecto a sus padres'
        while (i > 0 and self.H[self.parent(i)][0] < self.H[i][0]):
            self.swap(self.parent(i), i)
            i = self.parent(i)
        return

    def sift_down(self, i):
        'Filtrar hacia abajo, ordenar un elemento con respecto a sus hijos'
        maxIndex = i
        l = self.left_child(i)
        if l <= self.size - 1 and self.H[l][0] > self.H[maxIndex][0]:
            maxIndex = l
        r = self.right_child(i)
        if r <= self.size - 1 and self.H[r][0] > self.H[maxIndex][0]:
            maxIndex = r
        if i != maxIndex:
            self.swap(i,maxIndex)
            self.sift_down(maxIndex)
        return

    def insert(self, p):
        'Inserta un nuevo elemento al heap'
        
        #Redimensionar el arreglo cuando supere el tamaño final
        if self.size == self.max_size:
            self.H = self.H + ([None]*self.max_size)
            self.max_size = self.max_size*2
        self.size = self.size + 1
        self.H[self.size - 1] = p
        self.sift_up(self.size - 1)
        return

    def extract_max(self, val = None):
        'Extrae el valor maximo del heap'
        if self.size == 0:
            return None
        result = self.H[0]
        self.H[0] = self.H[self.size - 1]
        self.size = self.size - 1
        self.sift_down(0)
        #Si se hizo un remove pantes de llamar a extractmax
        if val is not None:
            result[0] = val
        return result
    
    def get_max(self):
        'Devuelve el key maximo'
        if self.size == 0:
            return None
        return self.H[0]

    def remove(self, i):
        'Remueve el elemento con indice i'
        # tmp guarda el valor del nodo a remover
        tmp = self.H[i][0]
        self.H[i][0] = self.H[0][0] + 1 
        self.sift_up(i)
        self.extract_max(tmp)
        return

    def change_priority(self, i, p):
        'Cambia la prioridad del elemento en el indice i por la prioridad p'
        oldp = self.H[i][0]
        self.H[i][0] = p
        if p > oldp:
            self.sift_up(i)
        else:
            self.sift_down(i)
        return

    def __str__(self):
        if self.size == 0:
            return 'Empty heap'
        pisos = 1
        size = self.size
        while size > 1:
            size = size // 2
            pisos = pisos + 1

        piso = 1
        cadena = ""
        for i in range(self.size):
            if self.H[i] is None:
                break
            if piso == pisos:
                cadena = cadena + str(self.H[i]) + " "

            else:
                if i in (2**(piso - 1) - 1, 0):
                    cadena = cadena + (" " * (2**(pisos-piso) - 1))
                    cadena = cadena + str(self.H[i])
                else:
                    cadena = cadena + (" " * (2**(pisos-piso+1) - 1))
                    cadena = cadena + str(self.H[i])

            if i == (2**(piso) - 2):
                piso = piso + 1
                cadena = cadena + "\n"

        return cadena

    def __repr__(self):
        if self.size == 0:
            return 'Empty heap'
        pisos = 1
        size = self.size
        while size > 1:
            size = size // 2
            pisos = pisos + 1

        piso = 1
        cadena = ""
        for i in range(self.size):
            if self.H[i] is None:
                break
            if piso == pisos:
                cadena = cadena + str(self.H[i][0]) + " "

            else:
                if i in (2**(piso - 1) - 1, 0):
                    cadena = cadena + (" " * (2**(pisos-piso) - 1))
                    cadena = cadena + str(self.H[i][0])
                else:
                    cadena = cadena + (" " * (2**(pisos-piso+1) - 1))
                    cadena = cadena + str(self.H[i][0])

            if i == (2**(piso) - 2):
                piso = piso + 1
                cadena = cadena + "\n"

        return cadena

    def ExtractMaxValues(self):
        '''
        Retorna una lista con todos arreglos [volumen,usuario] de los usuarios con el volumen maximo en la estructura.
        '''
        valueslist = []
        if self.get_max() is None:
            return valueslist
        maxvalue = self.get_max()
        
        #Aqui se comparan volumenes
        while self.get_max() is not None and maxvalue[0] == self.get_max()[0]:
            #Lo eliminamos y se añade a la lista
            nextvalue = self.extract_max()
            valueslist.append(nextvalue)
        
        return valueslist

#if __name__ == "__main__":
#    heap = MaxHeap(10)
#    keys = [[635,"e"],[4523,"a"],[4523,"z"],[4523,"c"],[4523,"d"],[4523,"e"],[4523,"f"],[4523,"g"],[4523,"h"],[4523,"i"],[4523,"j"],[4523,"k"],[235,"f"],[635,"d"],[589,"a"],[806,"z"],[543,"c"],[543,"w"],[123,"t"],[243,"y"],[2357,"i"],[54,"p"],[33,"q"],[21,"l"],[111,"j"],[406,"g"]]
#    for i in keys:
#        heap.insert(i)
#    print("estado inicial")
#    print(repr(heap))
#    #print("valores maximos")
#    #print("Valor maximo es:", heap.get_max())
#    #print(heap.extract_max())
#    #print("Valor maximo es:", heap.get_max())
#    #print(heap.extract_max())
#    #print("Valor maximo es:", heap.get_max())
#    #print(heap.extract_max())
#    print("Valores extraidos:\n",heap.ExtractMaxValues(),"\n\n")
#    print("nuevo arreglo")
#    print(repr(heap))
#    print("Valor maximo es:", heap.get_max())
