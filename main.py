"""
A los 21 dias de OCT de 2019


Se crea la clase interfaz grafica
Se declara self.telaMAPA :

                Cumple la funcion de pintar el mapa de la casa
                Se pinta primero las lineas x,y y sus respectivas leyendas(0,1,2,3 ...)


Se declara un metodo capaz de pintar todos los botones en el eje x, y

Se declara un metodo capaz de detectar si los botones han sido clickeados 

                self.click: 1 - ver todo el vector self.bononesPlanoXY
                            2 - determinar si hay un click
                            3 - determinar quien fue clickeado


Se declara la convencion de colores

0 blanco
1 verde
2 rojo
3 negro


Se declara el metodo update_graphic que actualiza la pantalla cada x milisegundos


"""

# Se importa lo que grafica
from tkinter import *
# Se importa aquello que frena la velocidad de ejecucion
from time import *
# Se importa el arbol
from Arbol import *


class Software:
    def __init__(self):
        # Pantalla principal
        self.pantalla = Tk()
        # Parte donde se grafican los interiores
        self.telaMAPA = Canvas(self.pantalla, height=600, width=700, bg="snow")
        # a la tela mapa se le agrega el evento touch
        self.telaMAPA.bind_all("<Button-1>", self.click)
        # Parte donde se grafican los controles, Agregar, Eliminar, Modificar
        self.telaPANELDECONTROL = Canvas(self.pantalla, height=600, width=200, bg="blue2")
        self.btnADDpunto = Button(self.telaPANELDECONTROL, text="Agregar", command=self.modoAgregarPuntos)
        self.btnEliminarPunto = Button(self.telaPANELDECONTROL, text="Eliminar", command=self.modoEliminarPuntos)
        self.btnVerArbol = Button(self.telaPANELDECONTROL, text="Ver Arbol", command=self.verElArbol)
        self.btnRepresetar = Button(self.telaPANELDECONTROL, text="PINTAR PAREDES", command=self.representarArbolAutomatico)
        self.btnRepresetarPasoAPaso = Button(self.telaPANELDECONTROL, text="Paso a Paso", command=self.representarArbolPasoAPaso)
        """
        Variables
        """
        
        """
        self.bononesPlanoXY :
            Se encarga de recopilar la informacion de los botones posx, poxy, informacion
            posx : Es la posicion en el eje x que ocupa
            posy : Es la posicion en el eje y que ocupa
            informacion: como tal el tag x-y que ocupan asi el boton 7,18 sera String 7-18
            Nota: todos los botones tienen una dimencion de 10x5 pixeles
        """
        self.bononesPlanoXY = []
        # Son demasiados botones por ello no se puede dar click muy rapido este 
        # Boleano controla que el click no se de muy seguido
        self.puedoClickear = True
        """
        self.option:
            Se encarga de realizar una accion deacuerdo a lo que diga el panel de control
            1 > se quiere agregar un elemento
            2 > se quiere eliminar un elemento
        """
        self.option = 0
        # Esto es el elemento sobre el que se realiza la opcion
        self.elementoSeleccionado = None
        # Esto controla que solo pueda ser seleccionado 1 elemento a la vez
        self.tempSelected = None
        # Esto controla si la forma de pintar es paso a paso o en automatico
        # self.stepByStep = False >> Se pinta en automatico
        # self.stepByStep = True >> Se pinta paso a paso
        self.stepByStep = False
        """
        Aqui estara el arbol
        """
        self.arbol = Arbol()
        """
        Aqui esta la variable que controla la pintada de las paredes
        1 - se rellena por defecto (0, x-y) 0: esta libre, x>tagx y>tagy
        2 - se captura todos los puntos del arbol
        3 - se pone el primer punto y se empieza a pintar sea x o y hasta que el pitado de la pared este listo

        """
        self.matrixMAPA = []
        self.pintadoDeParedesListo = False
        # Aqui se guardan los colores
        self.colores = ["white", "green", "red", "black"]
        """
        Fin de la declaracion de variables
        """


        # Mostramos lo declarado
        self.PINTARPANTALLA()

    
    def PINTARPANTALLA(self):
        """
        Vamos a pintar la pantalla, dimenciones, bonotes
        y aspectos generales
        """
        # Se configura la pantalla principal
        self.pantalla.title("Modelado de interiores")
        self.pantalla.geometry("900x600")

        # Se configura la pantalla del mapa interior
        self.telaMAPA.place(x=0, y=0)

        # Se configura la pantalla de control
        self.telaPANELDECONTROL.place(x=700, y=0)
        self.btnADDpunto.place(x=20, y=20)
        self.btnEliminarPunto.place(x=100, y=20)
        self.btnVerArbol.place(x=50, y=500)
        self.btnRepresetar.place(x=20, y=100)
        self.btnRepresetarPasoAPaso.place(x=20, y=140)
        # Se pintan las lineas
        self.PINTARLEYENDAPLANOXY()
        # Se lanza el evento que actualiza la pantalla
        self.pantalla.after(0, self.update_graphic)
        self.pantalla.mainloop()


    
    def update_graphic(self):
        """
        Este metodo actualiza la pantalla cada x milisegundos.
        Ojo: aqui se comprueba como esta la self.matrixMAPA y luego es representada
        """
        for i in self.matrixMAPA:
            for j in i:
                # Capturo el item
                item = self.telaMAPA.find_withtag(j[1])
                # Lo pinto del color necesario
                self.telaMAPA.itemconfigure(item, fill=self.colores[j[0]])
                
        self.pantalla.after(60, self.update_graphic)


    def PINTARLEYENDAPLANOXY(self):
        """
        Vamos a pintar todo lo referente los x, y
        1 - vamos a pintar los ejes x, y
        2 - vamos a pintar los numeritos que hay a los lados de los ejes
        3 - vamos a llamar un metodo que pinta la matrix de botones
        """
        
        # Pinto la linea del eje X
        self.telaMAPA.create_line(40, 560, 680, 560)

        # Pinto los numeros del eje x
        for i in range(0, 26):
            # Lugar de referencia a pintar que se mueve en x
            x0 = ((i+1)*24) + 30
            self.telaMAPA.create_text(x0, 580, text=str(i))

        
        # Pinto la linea del eje y
        self.telaMAPA.create_line(40, 20, 40, 560)

        # Pinto los numeros del eje y
        for i in range(0, 26):
            # Lugar de referencia a pintar
            y0 = ((i+1)*21) + 6
            self.telaMAPA.create_text(20, y0, text=str(25 - i))

        
        # Vamos a pintar la botonera
        self.PINTARMATRIXDEBOTONES()

        # Vamos a rellenar la matrix que controla el pintado de las paredes
        self.rellenarMatrix()


    def PINTARMATRIXDEBOTONES(self):
        """
        Este metodo se encarga de pintar todos los botones en la pantalla 
        """
        for i in range(0, 26):
            for j in range(0, 26):
                x0 = ((i+1)*24) + 26
                y0 = ((j)*21) 
                self.telaMAPA.create_rectangle(x0, 545 - y0, x0 + 10, 550 - y0, tag=str(i)+"-"+str(j))
                # Se guarda la inforamcion
                info = (x0, 545 - y0, str(i)+"-"+str(j))
                self.bononesPlanoXY.append(info)


    def rellenarMatrix(self):
        """
        Este metodo se encarga de rellenar la matrix que controla las 
        lineas que representan las paredes del interior

        (a, b)

        a > puede ser 0 o 1 : cero significa libre 1 significa pares
        b > tupla str(x-y)  x>pos en x donde estoy parado y>pos y donde estoy parado
        """
        for i in range(0, 26):
            self.matrixMAPA.append([])
            for j in range(0, 26):
                self.matrixMAPA[i].append((0, str(i)+"-"+str(j)))

    def reiniciarMatrix(self):
        """
        Este metodo dela la matrix al vacio
        """
        self.matrixMAPA = []
        self.rellenarMatrix()

    def click(self, Event):
        """
        Si la pantalla del mapa es clickeada con el mouse brinca este metodo
        """
        # Busco entre todos los botones cual fue clickeado
        if self.puedoClickear:
            self.puedoClickear = False
            
            # Se captura el click del mouse
            _mouseClick = (Event.x, Event.y)

            for i in self.bononesPlanoXY:
                r = (i[0], i[1])
                if self.colisiona(r, _mouseClick):
                    try:
                        # Ojo se acaba de clickear un elemento por ello lo seleccionamos
                        self.selected(i[2])
                        # El elemento fue seleccionado se procede a ejecutar la opcion
                        self.ejecutarOperacion()
                        # Un punto acaba de ser seleccionado se le marca de color morado
                        self.marcarPunto()
                    except:
                        print("Espere...")
                    
            self.puedoClickear = True 

    def colisiona(self, r, p):
        """
        r es un punto casteado a rectangulo x,y, x+10>>h
        p es un punto

        si el p esta dentro de r1 significa que se dio click
        """
        # Esta en el eje de las x?
        if p[0] >= r[0] and p[0] <= r[0] + 10:
            # Esta en el eje de las y?
            if p[1] >= r[1] and p[1] <= r[1] + 5:
                return True
            else:
                return False
        else:
            return False


    def selected(self, item):
        """
        Este metodo se encarga de seleccionar un item para hacerle algo
        """
        self.elementoSeleccionado = item

    def modoAgregarPuntos(self):
        """
        Supongase que el usuario desea agregar un punto al MAPA.
        Ello implica que el option sea 1
        """
        self.option = 1
        self.btnADDpunto['bg'] = "red"
        self.btnEliminarPunto['bg'] = "white"

    def modoEliminarPuntos(self):
        """
        Supongase que el usuario desea eliminar un punto al MAPA.
        Ello implica que el option sea 2
        """
        self.option = 2
        self.btnADDpunto['bg'] = "white"
        self.btnEliminarPunto['bg'] = "red"


    def ejecutarOperacion(self):
        """
        El usuario procedio a seleccionar un punto en el mapa y una opcion por ello
        """

        if self.option == 1:
            """
            El usuario desea agregar un punto al mapa
            """
            # Capturo los x, y
            k = self.elementoSeleccionado.split("-")
            x = int(k[0])
            y = int(k[1])
            # Ya capture los valores los agrego al arbol
            self.arbol.ADD((x, y))


        if self.option == 2:
            """
            El usuario desea eliminar un punto del mapa
            """
            pass

        print(self.option)
        print(self.elementoSeleccionado)


    def verElArbol(self):
        """
        El arbol cuando se construye se tagea con los x, y
        recurpero esos puntos y procedo a pintarlos  en un toplevel
        """
        ventanaEmergente = Toplevel()
        ventanaEmergente.title("Arbol")
        ventanaEmergente.geometry("500x500")
        tela = Canvas(ventanaEmergente, height=500, width=500, bg = "snow")

        # Capturo los nodos del arbol
        for i in self.arbol.returnXYDeNodos():
            # Pinto un circulo
            tela.create_oval(i[0], i[1], i[0]+55, i[1]+55)
            # SE pinta la leyenda
            tela.create_text(i[0]+24, i[1]+20, text=str(i[2]))


        tela.place(x=0, y=0)


    def representarArbolAutomatico(self):
        """
        Si el arbol esta listo, hay valores en el arbol
        los valores van a ser capturados y luego reprensentados en una matrix

        """
        if not self.stepByStep:
            print("Pintar paredes en auto")
        # Reinicio la matrix
        self.reiniciarMatrix()
        if self.arbol.raiz.data != None:
            # Capturo todos los valores
            for i in self.arbol.returnArbolComoVector():
                
                # Esta variable captura si se debe de pintar en x o y
                xy = int(i[1])
                cordenadas = i[0]
                print("===========NODOS DEL ARBOL=============")
                print(i)
                print("===========NODOS DEL ARBOL=============")
                # Se pinta en x o y?
                if xy == 0:
                    self.crearParedX(int(cordenadas[0]), int(cordenadas[1]))
                else:
                    self.crearParedY(int(cordenadas[0]), int(cordenadas[1]))

                self.esperarUnRato()

            print("========LISTO PARA PINTAR EL SIGUIENTE================")
            
        else:
            print("Arbol vacio")

    def representarArbolPasoAPaso(self):
        """
        Este metodo hace que se ejecute paso a paso la 
        creacion de los muros
        1 - un boleano controla si se hace o no paso a paso
        2 - el color del boton paso a paso indica el estado
        3 - se activa un sleep(x)
        """
        print("Paso a Paso")
        if self.stepByStep:
            self.stepByStep = False
            self.btnRepresetarPasoAPaso['bg'] = "white"
        else:
            self.stepByStep = True
            self.btnRepresetarPasoAPaso['bg'] = "red"

    def crearParedX(self, posx, posy):
        """
        Este metodo se mete a self.matrixMAPA y se para en el punto x,y luego rellena todo el eje x
        """

        # Marco el punto como nodo y guardo
        k = (3, self.matrixMAPA[posx][posy][1])
        self.matrixMAPA[posx][posy] = k


        # Pinto hacia -x hasta que termine o hasta que encuentre un muro
        for i in range(0, posy):
            
            iterator = (posy-1) - i
            # Capturo el punto
            # Si no es pared continue
            k = self.matrixMAPA[posx][iterator]
            # Si el valor esta permitido pinte si no termine
            if k[0] != 1 and k[0] != 2 and k[0] != 3:
                # Marco como pared
                alpha = (2, self.matrixMAPA[posx][iterator][1])
                # Guardo lo marcado
                self.matrixMAPA[posx][iterator] = alpha
            else:
                break

        # Pinto hacia +x 
        for j in range(posy+1, len(self.matrixMAPA[posx])):
            # Capturo el valor
            k = self.matrixMAPA[posx][j]
            # Si el valor esta permito pinte 
            if k[0] != 1 and k[0] != 2 and k[0] != 3:
                # marco como pared
                alpha = (2, self.matrixMAPA[posx][j][1])
                # Guardo
                self.matrixMAPA[posx][j] = alpha
            else:
                break

    def crearParedY(self, posx, posy):
        """
        Se pinta la pared en y
        """
        # Marco el punto como nodo y guardo
        print("Punto a pintar en y", posx, posy)
        k = (3, self.matrixMAPA[posx][posy][1])
        self.matrixMAPA[posx][posy] = k 

        # Procedo a marcar todo hacia -y
        for i in range(0, posx):
            pivote = (posx-1) - i
            k = self.matrixMAPA[pivote][posy]
            # Si esta permitido marco como muro
            if k[0] != 1 and k[0] != 2 and k[0] != 3:
                # Marco como muro
                alpha = (2, k[1])
                # Guardo
                self.matrixMAPA[pivote][posy] = alpha
            else:
                break

        # Procedo a marcar todo hacia +y
        for i in range(posx+1, len(self.matrixMAPA[0])):
            # Capturo
            k = self.matrixMAPA[i][posy]
            # Si esta permitido marco como muro
            if k[0] != 1 and k[0] != 2 and k[0] != 3:
                # marco como muro
                alpha = (2, k[1])
                self.matrixMAPA[i][posy] = alpha
            else:
                break

    def esperarUnRato(self):
        """
        Este metodo espera un rato
        """
        if self.stepByStep:
            sleep(0.7)
            self.telaMAPA.update()
            self.pantalla.update()


    def marcarPunto(self):
        """
        Este metodo marca 1 solo punto en el mapa.
        Y en caso de seleccionar otro punto se desmarca el anterior y se marca el nuevo
        """
        # Es primera vez que marco
        if self.tempSelected == None:
            # Capturo el ultimo elemento se se selecciono
            self.tempSelected = self.telaMAPA.find_withtag(self.elementoSeleccionado)
            # Lo Pinto
            self.telaMAPA.itemconfigure(self.elementoSeleccionado, fill="purple")
        else:
            # Desmarco el anterior
            self.telaMAPA.itemconfigure(self.tempSelected, fill="white")
            # Marco el nuevo
            self.tempSelected = self.telaMAPA.find_withtag(self.elementoSeleccionado)
            # Lo Pinto
            self.telaMAPA.itemconfigure(self.elementoSeleccionado, fill="purple")


# Lanzamos el software
s = Software()