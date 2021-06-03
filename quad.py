class Node():


    def __init__(self, dato):

        self.dato = dato
        self.uno = None
        self.dos = None
        self.tres = None
        self.cuatro = None


class QuadTree():



    def __init__(self, dato):

        self.raiz = Node(dato)
        self.dato=dato
 

    def __nuevo(self, node, dato1, dato2, dato3, dato4):

        node.uno = QuadTree(dato1)
        node.dos = QuadTree(dato2)
        node.tres = QuadTree(dato3)
        node.cuatro = QuadTree(dato4)

        


    def __buscar(self, nodo, busqueda):


        if(nodo.dato == busqueda):
            return nodo

        if(nodo.uno.dato == busqueda):

            return nodo.uno

        if(nodo.dos.dato == busqueda):

            return nodo.dos

        if(nodo.tres.dato == busqueda):

            return nodo.tres

        if(nodo.cuatro.dato == busqueda):

            return nodo.cuatro



    def nuevo_(self, dato1, dato2, dato3, dato4):

        self.__nuevo(self.raiz, dato1, dato2, dato3, dato4)

    
    def buscar_(self, busqueda):

        return self.__buscar(self.raiz, busqueda)

    
