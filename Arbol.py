"""
a los 18 dias de oct de 2019

Se declara una estructura de tipo nodo que sera Kernel de un arbol

>>Se comprobo el funcionamiento de esto por ello se agregan los valores 
que seran los encargados de graficar

>>Condicion para no almacenar nodos repetidos

"""

class Nodo:
    def __init__(self):
        """
        Variables correspondientes a la informacion del nodo
        """
        self.IZQ = None
        self.data = None
        self.etiqueta = None
        self.DER = None
        self.padre = None
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
        
    def getLabel(self):
        return self.etiqueta
    
    def getParent (self):
        return self.padre
    
    def getRightChild(self):
        return self.DER
    
    def getLeftChild(self):
        return self.IZQ
        
    def setLabel(self, label):
        self.etiqueta = label
    
    def setParent (self, parent):
        self.padre = parent
    
    def setRightChild(self, child):
        self.DER = child
        
    def setLeftChild(self, child):
        self.IZQ = child
        
    def hasRightChild(self):
        return self.DER
        
    def hasLeftChild(self):
        return self.IZQ
        
    def getBF(self):
        return self._bf
    
    def setBF(self, bf):
        self._bf = bf
    
    def isRightChild(self):
        return(self.getParent().hasRightChild() and self.etiqueta == self.DER)
        
    def isLeftChild(self):
        return(self.getParent().hasLeftChild() and self.etiqueta == self.IZQ)
    
    def isLeaf (self):
        return (not self.DER and not self.IZQ)

        
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
        # Si se desea buscar un nodo aqui quedara guardado
        self.nodoTemporal = None

    # Este metodo agrega un valor al arbol
    def ADD(self, x, label):
        # raiz, dato a agregar (x, y), eje, nivel, referencia pintado
        self._ADD(self.raiz, x, label, 0, 0, 160, self.raiz)
    # Este metodo es el que en realidad agrega el nodo al arbol
    # Ojo: Solo cuando se carga desde JSON el label tiene valor
    def _ADD(self, NODO, x, label, eje, nivel, newPosX, padre):
        # Si la raiz esta vacia pues se crea
        if(self.raiz.data == None):
            """
            Esto significa que el arbol aun no existe.
            Creo la raiz con la data que es una tupla
            Genero una posicion x, y que solo sirve para visualizar el arbol
            la raiz queda asociada en automatico en eje x : 0
            """
            self.raiz.data = x
            self.raiz.etiqueta = label
            self.raiz.padre = padre
            self.raiz.eje = 0
            self.nivel = 0
            self.raiz.posx = 320
            self.raiz.posy = 20
            self.numeroDeNodos = 1
        else:
            # Ojo: No se guardan repetidos
            if NODO.data == x:
                return None

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
                        self._ADD(NODO.DER, x, NODO.etiqueta, 1, nivel, newPosX ,NODO.padre)
                     
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
                        self._ADD(NODO.IZQ, x,NODO.etiqueta,  1, nivel, newPosX, NODO.padre)

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
                        self._ADD(NODO.DER, x, NODO.etiqueta, 0, nivel, newPosX, NODO.padre)
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
                        self._ADD(NODO.IZQ, x,NODO.etiqueta, 0, nivel, newPosX, NODO.padre)


    def buscarNodo(self, data):
        """
        Este metodo busca un nodo y luego lo retorna
        """
        self.nodoTemporal = None
        self._buscarNodo(self.raiz, data)
        return self.nodoTemporal

    def _buscarNodo(self, NODO, data):
        # Si lo encontro retorne sino busquelo
        if NODO.data == data:
            self.nodoTemporal = NODO
        else:
            if NODO.DER != None:
                self._buscarNodo(NODO.DER, data)
            if NODO.IZQ != None:
                self._buscarNodo(NODO.IZQ, data)


    def modificarData(self, x, newX):
        """
        Este metodo le entra x que es un valor que existe en el arbol
                             newX que es el nuevo valor que va a existir en el arbol

                             Se busca el x y newX, x tiene que existir y newX no puede existir. 
        """
        """Si el valor viejo existe EXISTE"""
        k = self.buscarNodo(x)
        """Si el valor nuevo no existe"""    
        m = self.buscarNodo(newX)
        if k != None and m == None:
            print("Modificando")
            k.data = newX


    def invertirEjesArbol(self):
        self._invertirEjesArbol(self.raiz)

    def _invertirEjesArbol(self, NODO):
        if NODO != None:
            if NODO.eje == 0:
                NODO.eje = 1
            else:
                NODO.eje = 0

            self._invertirEjesArbol(NODO.DER)
            self._invertirEjesArbol(NODO.IZQ)


    def eliminarNodo(self, data):
        """
        Este metodo es muy diferente al buscar, aqui tenemos que capturar el hijo 
        desde el padre... eliminaremos el hijo.
        """
        self.nodoTemporal = None
        self._BuscarParaEliminar(self.raiz, data)

        if self.nodoTemporal != None:
            # Caso Es la raiz y no tiene hijos
            if self.nodoTemporal == self.raiz:
                if self.raiz.DER == None and self.raiz.IZQ == None:
                    self.raiz = None
            else:
                # Sera que esta a la derecha?
                if self.nodoTemporal.DER != None:
                    if self.nodoTemporal.DER.data == data:
                        # Si el nodo es una hoja pues simplemente lo elimino
                        if self.nodoTemporal.DER.DER == None and self.nodoTemporal.DER.IZQ == None:
                            self.nodoTemporal.DER = None
                            return True

                        # Si el nodo tiene un unico hijo pues simplemente reemplazo
                        tieneNietoDER = self.nodoTemporal.DER.DER != None and self.nodoTemporal.DER.IZQ == None
                        tieneNieroIZQ = self.nodoTemporal.DER.DER == None and self.nodoTemporal.DER.IZQ != None

                        if tieneNietoDER or tieneNieroIZQ:
                            if tieneNietoDER:
                                self.nodoTemporal.DER = self.nodoTemporal.DER.DER 
                                return True

                            if tieneNieroIZQ:
                                self.nodoTemporal.DER = self.nodoTemporal.DER.IZQ
                                return True

                        print("ESTA A LA DERECHA PARA ELIMINAR")

                #Sera que esta a la izquierda?
                if self.nodoTemporal.IZQ != None:
                    if self.nodoTemporal.IZQ.data == data:
                        # Si el nodo es una hoja pues simplemente lo elimino
                        if self.nodoTemporal.IZQ.DER == None and self.nodoTemporal.IZQ.IZQ == None:
                            self.nodoTemporal.IZQ = None

                        # Si el noxo tiene un unico hijo pues reemplazo

                        tieneNietoDER = self.nodoTemporal.IZQ.DER != None and self.nodoTemporal.IZQ.IZQ == None
                        tieneNietoIZQ = self.nodoTemporal.IZQ.DER == None and self.nodoTemporal.IZQ.IZQ != None
                        
                        # Reemplazo hijo por nieto
                        if tieneNietoDER or tieneNietoIZQ:
                            if tieneNietoDER:
                                self.nodoTemporal.IZQ = self.nodoTemporal.IZQ.DER
                                return True

                            if tieneNietoIZQ:
                                self.nodoTemporal.IZQ = self.nodoTemporal.IZQ.IZQ
                                return True

                        print("Esta a la IZQ PRA ELIMINAR")

        # Como no encontro nada pues retorno falso
        return False

    def _BuscarParaEliminar(self, NODO, data):
        """
        Este metodo es mas diferente xq yo los capturo por el padre 
        y le borro el hijo
        """
        # Sera que es la raiz?
        if self.raiz.data == data:
            self.nodoTemporal = NODO
        else:
            # Tiene derecha?
            if NODO.DER != None:
                # Sera que es el de la derecha?
                if NODO.DER.data == data:
                    self.nodoTemporal = NODO
                else:
                    # Busquelo por la derecha
                    self._BuscarParaEliminar(NODO.DER, data)
                
            # Tiene IZQ
            if NODO.IZQ != None:
                # Sera que es el de la izq
                if NODO.IZQ.data == data:
                    self.nodoTemporal = NODO
                else:
                    # busquelo por la izquierda
                    self._BuscarParaEliminar(NODO.IZQ, data)


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

    def removeNode (self, label):
        if(self.raiz != None):
            targetNode = self.searchNode(label)
            if(targetNode):
                self._removeNode(targetNode)
            else:
                print("Element with label ", label, "does not exists!")
        else:
            print ("The tree is empty.")
            
    def _removeNode(self, NODO):
        if(NODO.isLeaf()):
            if(NODO.isLeftChild()):
                NODO.getParent().setLeftChild(None)
                #a mi padre le digo que ya no tiene hijo izquierdo
                #Debo borrarlo en ambos sentidos el padre deja al hijo y 
                #el hijo deja al padre
            else:
                NODO.getParent().setRightChild(None)
            NODO.setParent(None)
                #A mi me digo que ya no tengo papá
        else:
            if(NODO.hasLeftChild() and NODO.hasRightChild()):
                #si tiene los dos hijos se busca el sucesor
                suc = self._getSucessor(NODO.hasRightChild())
                self._updateNode(NODO, suc)
                if(suc.isLeaf()):
                    suc.getParent().setLeftChild(None)
                    suc.setParent(None)
                    #Si es hoja sólo quito la referencia de su hijo izquierdo
                else:
                    suc.getParent().setLeftChild(suc.hasRightChild())
                    #Padre, ponga como su hijo izquierdo al hijo derecho del sucesor
                    suc.hasRightChild().setParent(suc.getParent())
                    #y le dice al ihjo cuál va a ser su padre
                    suc.setRightChild(None)
                    suc.setParent(None)
                    #borro referencias tanto del padre como del hijo
            else:
                if(NODO.isLeftChild()):
                    if(NODO.hasLeftChild()):
                        NODO.getParent().setLeftChild(NODO.hasLeftChild())
                        NODO.hasLeftChild().setParent(NODO.getParent())
                        NODO.setLeftChild(None)
                        #quita referencia
                    else:
                        NODO.getParent().setLeftChild(NODO.hasRightChild())
                        NODO.hasRightChild().setParent(NODO.getParent())
                        NODO.setRightChild(None)
                else:
                    if(NODO.hasLeftChild()):
                        NODO.getParent().setRightChild(NODO.hasLeftChild())
                        NODO.hasLeftChild().setParent(NODO.getParent())
                        NODO.setLefttChild(None)
                    else:
                        NODO.getParent().setRightChild(NODO.hasRightChild())
                        NODO.hasRightChild().setParent(NODO.getParent())
                        NODO.setRightChild(None)
                NODO.setParent(None)
                #sea cual sea el caso, al fin el nodo se tiene que desprender de su padre
               
                
    def _updateNode(self, oldNode, newNode):
        #oldNode.setValue(newNode.getValue())
        oldNode.setLabel(newNode.getLabel())
            
    def _getSucessor (self, node):
        lc = node.hasLeftChild()
        if(lc):
            return self._getSucessor(lc)
        else:
            return node
        
    def searchNode(self, label):
        if(self.raiz):
            return self._searchNode(label, self.raiz)
        else:
            print("The tree is empty.")
            
    def _searchNode(self, label, parent):
        if(not parent):
            return None
        if(label == parent.getLabel()):
            return parent
        else:
            node = self._searchNode(label, parent.hasLeftChild())
            #busca por el hijo izquierdo
            if(not node):
                node = self._searchNode(label, parent.hasRightChild())
                #Y si no lo encuentra los busca por el hijo derecho
            return node