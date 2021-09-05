'''
Implementacion propia de arbol AVL
'''

class TreeNode:
    '''
    Nodo especial para arbol avl
    '''
    def __init__(self, key):
        self.height = 1
        self.key = key #[volumen,usuario]
        self.left = None
        self.right = None


class AVLTree:

    def __init__(self):
        self.root = None

    #Retorna True si el key nodo1 es mayor a nodo2
    #Compara primero el volumen y  luego los usuarios
    def comparador(self,nodo1key,nodo2key):
        if (nodo1key[0] > nodo2key[0]):
            return True
        elif(nodo1key[0] < nodo2key[0]):
            return False
        else: #si tienen igual valor volumen
        #Comparar por nombre o id
            if (nodo1key[1] > nodo2key[1]):
                return True
            elif(nodo1key[1] < nodo2key[1]):
                return False

    def insert(self, key):
        '''
        Llama la funcion recursiva interna para actualizar el valor
        '''
        self.root = self.insert_node(self.root, key)

    def insert_node(self, root, key):
        '''
        Inserta un nodo en el arbol avl con la raiz root
        '''
        if root is None:
            return TreeNode(key)
            #Verificar si key<root.key
        elif not self.comparador(key, root.key):
            root.left = self.insert_node(root.left, key)
        else:
            root.right = self.insert_node(root.right, key)

        root.height = 1 + max(self.get_Height(root.left),
                              self.get_Height(root.right))

        # Verificar balance del arbol
        balance = self.get_Balance(root)
        if balance < -1: #desbalance hacia la izquierda
              #Comparar key<root.left.key
            if not self.comparador(key, root.left.key):
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)

        if balance > 1: #Desbalance hacia la derecha
               #Comparar key > root.right.key
            if self.comparador(key, root.right.key):
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root

    def delete(self, key):
        '''
        Llama la funcion recursiva interna para actualizar el valor
        '''
        self.root = self.delete_node(self.root, key)

    def delete_node(self, root, key):
        '''
        Elimina un nodo que contenga la llave "key" en el arbol
        avl que tenga la raiz "rootj
        '''
        if root is None:
            return root
        if root.key == key:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right, temp.key)
            #Compara key < root.key
        elif not self.comparador(key, root.key):
            root.left = self.delete_node(root.left, key)
            #Compara key > root.key
        elif self.comparador(key, root.key):
            root.right = self.delete_node(root.right, key)

        root.height = 1 + max(self.get_Height(root.left),
                              self.get_Height(root.right))

        balance = self.get_Balance(root)
        #Cambios en balance
        if balance < -1: #desbalance hacia la izquierda
            if self.get_Balance(root.left) <= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance > 1: #desbalance hacia la derecha
            if self.get_Balance(root.right) >= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        return root

    def left_rotate(self, z):
        '''
        Rotacion a izquierda
        '''
        y = z.right
        tmp = y.left
        y.left = z
        z.right = tmp
        z.height = 1 + max(self.get_Height(z.left),
                           self.get_Height(z.right))
        y.height = 1 + max(self.get_Height(y.left),
                           self.get_Height(y.right))
        return y

    def right_rotate(self, z):
        '''
        Rotacion a derecha
        '''
        y = z.left
        tmp = y.right
        y.right = z
        z.left = tmp
        z.height = 1 + max(self.get_Height(z.left),
                           self.get_Height(z.right))
        y.height = 1 + max(self.get_Height(y.left),
                           self.get_Height(y.right))
        return y

    def is_empty(self):
        return self.root is None

    def get_Height(self, node):
        '''
        Obtiene la altura de un nodo
        '''
        if node is None:
            return 0
        return node.height

    def get_Balance(self, node):
        '''
        Obtiene el balance, esto es la diferencia entre la altura
        de su nodo izquierdo y su nodo derecho
        '''
        if node is None:
            return 0
        return self.get_Height(node.right) - self.get_Height(node.left)

    def minNode(self, root):
        if root is None or root.left is None:
            return root
        return self.minNode(root.left)

    def get_MinValueNode(self):
        return self.minNode(self.root).key

    def maxNode(self, root):
        if root is None or root.right is None:
            return root
        return self.maxNode(root.right)

    def get_MaxValueNode(self):
        if self.root is None:
            return self.root
        return self.maxNode(self.root).key

    def representation(self):
        self.print_repr(self.root, "", True)

    def print_repr(self, currNode, indent, right):
        '''
        Representacion basica de avl
        '''
        if currNode is not None:
            tmp = ""
            tmp = tmp + indent
            if right:
                tmp = tmp + "R----"
                indent += "     "
            else:
                tmp = tmp + "L----"
                indent += "|    "
            print(tmp, currNode.key, sep="")
            self.print_repr(currNode.left, indent, False)
            self.print_repr(currNode.right, indent, True)

    def ExtractMaxValues(self):
        '''
        Retorna una lista con todos arreglos [volumen,usuario] de los usuarios con el volumen maximo en la estructura.
        '''
        nodelist = []
        #Conocemos el valor del nodo maximo, y luego vemos si el maximo en el arbol tiene su mismo valor de volumen y lo añadimos a la lista
        if self.maxNode(self.root) is None:
            return nodelist

        maxnodevalue = self.get_MaxValueNode()
        #Aqui se comparan volumenes
        while self.maxNode(self.root) is not None and maxnodevalue[0] == self.get_MaxValueNode()[0]:
            #Lo eliminamos y se añade a la lista
            nextnodevalue = self.get_MaxValueNode()
            nodelist.append(nextnodevalue)
            self.delete(nextnodevalue)

        return nodelist

if __name__ == "__main__": #Pruebas del funcionamiento
    myTree = AVLTree()
    #keys = [[10,"pe"], [6,"a"],[12,"a"],[11,"a"]]
    keys = [[11,"a"]]
    keys = []

    for key in keys:
        myTree.insert(key)

    myTree.representation()
    #print("max value: ", myTree.get_MaxValueNode(), end="\n\n")
    print("max value: ", myTree.ExtractMaxValues(), end="\n\n")



    #print(myTree.ExtractMaxValues())
    #myTree.representation()
    myTree.delete([6,"a"])
    print("After Deletion: ")
    myTree.representation()

    #print("max value: ", myTree.get_MaxValueNode())
    #print("min value: ", myTree.get_MinValueNode())
