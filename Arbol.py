"""
a los 18 dias de oct de 2019

Se declara una estructura de tipo nodo que sera Kernel de un arbol

>>Se comprobo el funcionamiento de esto por ello se agregan los valores 
que seran los encargados de graficar

"""

class Nodo:
    def __init__(self):
        """
        Variables correspondientes a la informacion del nodo
        """
        self.IZQ = None
        self.data = None
        self.DER = None
        # Eje corresponde a si esta ubicado en x=0 o en y=1
        self.eje = 0
        """
        Variables x,y correspondientes a  graficas
        OJo: esto solo es para mostrar el arbol 
        no tiene nada que ver con el mapa de interiores
        """
        self.posx = 0
        self.posy = 0
        """
        Variables 
        """
        


"""
a los 18 dias de oct de 2019

Se declara una clase arbol que guarda tuplas de enteros a, b donde a y b pertenecen a los naturales

"""
class Arbol:
    def __init__(self):
        self.raiz = Nodo()
        self.numeroDeNodos = 0
        self.vectorPosNodos = []

    # Este metodo agrega un valor al arbol
    def ADD(self, x):
        # raiz, dato a agregar (x, y), eje
        self._ADD(self.raiz, x, 0, 110)
    # Este metodo es el que en realidad agrega el nodo al arbol
    def _ADD(self, NODO, x, eje, newPosX):
        # Si la raiz esta vacia pues se crea
        if(self.raiz.data == None):
            """
            Esto significa que el arbol aun no existe.
            Creo la raiz con la data que es una tupla
            Genero una posicion x, y que solo sirve para visualizar el arbol
            la raiz queda asociada en automatico en eje x : 0
            """
            self.raiz.data = x
            self.raiz.eje = 0
            self.raiz.posx = 220
            self.raiz.posy = 20
            self.numeroDeNodos = 1
        else:
            """
            Procedo a buscar un espacio disponible.

            1 - Miro si estoy parado en el eje x o en el y
            """

            if eje == 0:
                """
                Eje en 0 significa que voy a comparar con la componente en x
                """
                if NODO.data[0] <= x[0]:
                    # Si la derecha esta vacia guardelo
                    if NODO.DER == None:
                        # Creo un nodo nuevo
                        NODO.DER = Nodo()
                        # Meto el dato
                        NODO.DER.data = x
                        # Lo asocio con el eje y
                        NODO.DER.eje = 1
                        NODO.DER.posx = NODO.posx + newPosX 
                        NODO.DER.posy = NODO.posy + 50 
                        self.numeroDeNodos = 1 + self.numeroDeNodos 
                    else:
                        # La derecha no tiene espacio recalculo y mando al siguiente
                        newPosX = (int)(newPosX / 2)
                        self._ADD(NODO.DER, x, 1, newPosX)
                else:
                    # Si la izq esta vacia guarde
                    if NODO.IZQ == None:
                        # Creo un nodo nuevo
                        NODO.IZQ = Nodo()
                        # Guardo el dato
                        NODO.IZQ.data = x
                        # Lo asocio con el eje y
                        NODO.IZQ.eje = 1
                        NODO.IZQ.posx = NODO.posx - newPosX
                        NODO.IZQ.posy = NODO.posy + 50
                        self.numeroDeNodos = 1 + self.numeroDeNodos
                    else:
                        # La izquierda no tiene espacio recalculo y mando al siguiente
                        newPosX = (int)(newPosX / 2)
                        self._ADD(NODO.IZQ, x, 1, newPosX)

            else:
                """
                eje en 1 sinifica que voy a comprar con la componente en y
                """
                if NODO.data[1] <= x[1]:
                    # Si la derecha esta vacia guardelo
                    # Si la derecha esta vacia guardelo
                    if NODO.DER == None:
                        # Creo un nodo nuevo
                        NODO.DER = Nodo()
                        # Meto el dato
                        NODO.DER.data = x
                        # Lo asocio con el eje x
                        NODO.DER.eje = 0
                        NODO.DER.posx = NODO.posx + newPosX 
                        NODO.DER.posy = NODO.posy + 50 
                        self.numeroDeNodos = 1 + self.numeroDeNodos 
                    else:
                        # La derecha no tiene espacio recalculo y mando al siguiente
                        newPosX = (int)(newPosX / 2)
                        self._ADD(NODO.DER, x, 0, newPosX)
                else:
                    # Si la izq esta vacia guarde
                    if NODO.IZQ == None:
                        # Creo un nodo nuevo
                        NODO.IZQ = Nodo()
                        # Guardo el dato
                        NODO.IZQ.data = x
                        # Lo asocio con el eje x
                        NODO.IZQ.eje = 0
                        NODO.IZQ.posx = NODO.posx - newPosX
                        NODO.IZQ.posy = NODO.posy + 50
                        self.numeroDeNodos = 1 + self.numeroDeNodos
                    else:
                        # La izquierda no tiene espacio recalculo y mando al siguiente
                        newPosX = (int)(newPosX / 2)
                        self._ADD(NODO.IZQ, x, 0, newPosX)
                        
                        


    # Este metodo retorna los Nodos como puntos x,y en el plano
    def returnXYDeNodos(self):
        """
        Se retorna los nodos como puntos en el plano
        [ [x,y] , [x,y], [x,y] ,  ....  ]
        """
        self.vectorPosNodos = []
        self._returnXYDeNodos(self.raiz)
        return self.vectorPosNodos
    # Este metodo es el que busca los puntos x,y,valor
    def _returnXYDeNodos(self, NODO):
        if(NODO!=None):
            self.vectorPosNodos.append([NODO.posx, NODO.posy, NODO.data])
            self._returnXYDeNodos(NODO.IZQ)
            self._returnXYDeNodos(NODO.DER)



    # Este metodo es solo para pruebas
    def inorder(self):
        self._inorder(self.raiz)
    # Complemento del inorder
    def _inorder(self, NODO):
        if(NODO != None):
            self._inorder(NODO.IZQ)
            print(NODO.data)
            self._inorder(NODO.DER)



a  = Arbol()
a.ADD((5, 8))
a.ADD((10, 15))
a.ADD((1, 13))
a.ADD((20, 12))
a.ADD((11, 15))
a.ADD((14, 8))


a.inorder()