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
        # Esta variable corresponde al nivel
        self.nivel = 0
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
        # Retorna los nodos como x,y,data para graficar solo el arbol
        self.vectorPosNodos = []
        # Retorna el arbol como un vector para poder graficar el vector
        self.arbolVectorizado = []

    # Este metodo agrega un valor al arbol
    def ADD(self, x):
        # raiz, dato a agregar (x, y), eje, nivel, referencia pintado
        self._ADD(self.raiz, x, 0, 0, 110)
    # Este metodo es el que en realidad agrega el nodo al arbol
    def _ADD(self, NODO, x, eje, nivel, newPosX):
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
            self.nivel = 0
            self.raiz.posx = 220
            self.raiz.posy = 20
            self.numeroDeNodos = 1
        else:
            """
            Procedo a buscar un espacio disponible.
                1 - Verifico si debo comparar en x o en y

            """
            if NODO.eje == 0:
                """
                El nodo corresponde al eje x
                Comparo los valores en el eje x
                """
                if NODO.data[0] <= x[0]:
                    """
                    Este valor debe de ir a la derecha comparado eje x 
                    
                    """
                    # Miro si hay espacio
                    if NODO.DER == None:
                        print("Entro DER", NODO.data[0], x[0])
                        # Creo un nodo nuevo
                        NODO.DER = Nodo()
                        # Meto el dato
                        NODO.DER.data = x
                        # Lo asocio con el eje y
                        NODO.DER.eje = 1
                        # Le pongo el nivel
                        NODO.DER.nivel = nivel
                        NODO.DER.posx = NODO.posx + newPosX 
                        NODO.DER.posy = NODO.posy + 50 
                        self.numeroDeNodos = 1 + self.numeroDeNodos
                    else:
                        # No hay espacio busque donde meter esa wea
                        newPosX = (int)(newPosX / 2)
                        nivel = nivel + 1
                        self._ADD(NODO.DER, x, 1, nivel, newPosX)
                     
                else:
                    """
                    Este valor debe de ir a la izq comparado eje x
                    """
                    # Miro si hay espacio
                    if NODO.IZQ == None:
                        # Creo el Nodo
                        print("Entro izq", NODO.data[0], x[0])
                        NODO.IZQ = Nodo()
                        # Le metemos el 
                        NODO.IZQ.data = x
                        # Lo asocio con el eje y
                        NODO.IZQ.eje = 1
                        # Le pongo el nivel
                        NODO.IZQ.nivel = nivel
                        NODO.IZQ.posx = NODO.posx - newPosX 
                        NODO.IZQ.posy = NODO.posy + 50 
                        # Registro el Nodo
                        self.numeroDeNodos = 1 + self.numeroDeNodos
                    else:
                        # No hay espacio busque donde meterlo
                        newPosX = (int)(newPosX / 2)
                        nivel = nivel + 1
                        self._ADD(NODO.IZQ, x, 1, nivel, newPosX)

                    """
                    Fin de la condicion que agrega por el criterio de las x
                    """     
            else:
                """
                Ahora seguimos comparando con la componente en y
                """
                if NODO.data[1] <= x[1]:
                    # Hay espacio para la derecha?
                    if NODO.DER == None:
                        # Creo un nodo nuevo
                        NODO.DER = Nodo()
                        # Le metemos el 
                        NODO.DER.data = x
                        # Lo Asociamos con el eje x
                        NODO.DER.eje = 0
                        # Le ponemos el nivel
                        NODO.DER.nivel = nivel
                        # Para graficar el arbolito
                        NODO.DER.posx = NODO.posx + newPosX 
                        NODO.DER.posy = NODO.posy + 50 
                        # Registro en el contador de nodos
                        self.numeroDeNodos = 1 + self.numeroDeNodos
                    else:
                        # No hay espacio procedo a buscar
                        newPosX = (int)(newPosX / 2)
                        nivel = nivel + 1
                        self._ADD(NODO.DER, x, 0, nivel, newPosX)
                else:
                    # hay espacio pa la izq
                    if NODO.IZQ == None:
                        # Creo un nodo nuevo 
                        NODO.IZQ = Nodo()
                        # Metemos el dato
                        NODO.IZQ.data = x
                        # Lo asociamos con el eje x
                        NODO.IZQ.eje = 0
                        # Le ponemos nivel 
                        NODO.IZQ.nivel = nivel
                        NODO.IZQ.posx = NODO.posx - newPosX 
                        NODO.IZQ.posy = NODO.posy + 50 
                        # Registro en el contador de nodos
                        self.numeroDeNodos = 1 + self.numeroDeNodos
                    else:
                        # No hay espacio procedo a buscar
                        newPosX = (int)(newPosX / 2)
                        nivel = nivel + 1
                        self._ADD(NODO.IZQ, x, 0, nivel, newPosX)




    # Este metodo retorna el arbol como un vector
    def returnArbolComoVector(self):
        # Reinicio el arbol
        self.arbolVectorizado = []
        self._returnArbolComoVector(self.raiz)
        return self.arbolVectorizado

    # El vector se reccore en pre-order para vectorizar
    def _returnArbolComoVector(self, NODO):
        if NODO != None:
            k = [NODO.data, NODO.eje]
            self.arbolVectorizado.append(k)
            self._returnArbolComoVector(NODO.IZQ)
            self._returnArbolComoVector(NODO.DER)


                        
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