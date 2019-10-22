"""
A los 21 dias de OCT de 2019


Se crea la clase interfaz grafica
Se declara self.telaMAPA :

                Cumple la funcion de pintar el mapa de la casa
                Se pinta primero las lineas x,y y sus respectivas leyendas(0,1,2,3 ...)


Se declara un metodo capaz de pintar todos los botones en el eje x, y

Se declara un metodo capaz de detectar si los botones han sido clickeados


"""

# Se importa lo que grafica
from tkinter import *
# Se importa aquello que frena
from time import *


class Software:
    def __init__(self):
        # Pantalla principal
        self.pantalla = Tk()
        # Parte donde se grafican los interiores
        self.telaMAPA = Canvas(self.pantalla, height=600, width=700, bg="snow")
        # a la tela mapa se le agrega el evento touch
        self.telaMAPA.bind_all("<Button-1>", self.click)

        # Parte donde se grafican los controles, Agregar, Eliminar, Modificar

        """
        Variables
        """
        
        """
        self.bononesPlanoXY :
            Se encarga de recopolar la informacion de los botones posx, poxy, informacion
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

        # Se pintan las lineas
        self.PINTARLEYENDAPLANOXY()

        self.pantalla.mainloop()


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


    def PINTARMATRIXDEBOTONES(self):
        """
        Este metodo se encarga de pintar todos los botones en la pantalla 
        """
        for i in range(0, 26):
            for j in range(0, 26):
                x0 = ((i+1)*24) + 26
                y0 = ((j)*21) 
                self.telaMAPA.create_rectangle(x0, 545 - y0, x0 + 10, 550 - y0, tag="btn")
                # Se guarda la inforamcion
                info = (x0, 545 - y0, str(i)+"-"+str(j))
                self.bononesPlanoXY.append(info)


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
                    print("EPA")

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

        


# Lanzamos el software
s = Software()