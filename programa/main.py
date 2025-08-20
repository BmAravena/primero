class Jugador:
    def __init__(self, nombre, signo):
        self.nombre = nombre
        self.signo = signo
        
    def informacion(self):
        print(f"Nombre {self.nombre} Signo {self.signo}")

    def getNombre(self):
        return self.nombre
     
    def getSigno(self):
        return self.signo


class Signo:
    def __init__(self, tipo):
        self.tipo = tipo

    def getSigno(self):
        return self.tipo


class Tablero:
    def __init__(self, tamanio=3):
        self.tamanio = tamanio
        #self.celdas =  [["-"*tamanio] for _ in range(tamanio)]
        self.celdas = [["-" for _ in range(tamanio)] for _ in range(tamanio)]


    def muestraTablero(self):
        for fila in self.celdas:
            print('|'+" ".join(fila)+"|")
            #print(" | "+fila+" |")


    def verificaDisponibilidad(self, x, y):
        if self.celdas[x][y] == '-':
            return True
        else:
            return False


    def colocaSigno(self, x, y, signo):
        if self.verificaDisponibilidad(x,y):
            self.celdas[x][y] = signo
        else:
            print("celda ocupada")
    

    def verificaLineas(self, signo):
        cantidad = 0
        for linea in range(len(self.celdas)):
            for columna in range(len(self.celdas)):
                if self.celdas[linea][columna] == signo:
                    cantidad += 1
                    if cantidad == 3:
                        return True
                    
            cantidad = 0

        return False


    def verificaColumnas(self, signo):
        cantidad = 0
        for fila in range(len(self.celdas)):
            for columna in range(len(self.celdas)):
                if self.celdas[columna][fila] == signo:
                    cantidad += 1
                    if cantidad == 3:
                        return True
            cantidad = 0

        return False
    
    
    def verificaDiagonales(self, signo):
        if self.celdas[0][0] == signo and self.celdas[1][1] == signo and self.celdas[2][2] == signo:
           return True

        elif self.celdas[0][2] == signo and self.celdas[1][1] == signo and self.celdas[2][0] == signo:
           return True
        
        return False
        

    def verificaGanador(self, signo):
        if (self.verificaColumnas(signo) or self.verificaLineas(signo) or self.verificaDiagonales(signo)):
            return True
        
        return False
    

    def lleno(self):
        for fila in self.celdas:
            if fila == '-':
                return False
            
        return True



class Juego:
    def __init__(self, primer_jugador, segundo_jugador):
        self.primer_jugador = primer_jugador
        self.segundo_jugador = segundo_jugador
    
    def main(self, tablero):
        fLag = True
        turno = True

        while fLag:
            if turno:
                print("Turno del primer jugador")
                signo = self.primer_jugador.getSigno()
            else:
                print("Turno del segundo jugador")
                signo = self.segundo_jugador.getSigno()

            try:
                x = int(input("Ingresa posición en x: "))
                y = int(input("Ingresa posición en y: "))
                tablero.colocaSigno(x, y, signo)
                tablero.muestraTablero()
                
            except Exception as e:
                print(f"ERROR: {e}")


            if tablero.verificaGanador(signo):
                tablero.muestraTablero()
                if signo == self.primer_jugador.getSigno():
                    print("Hay ganador!, el primer jugador")
                    self.primer_jugador.informacion()
                else:
                    print("Hay ganador!, el segundo jugador")
                    self.segundo_jugador.informacion()

                fLag = False


            turno = not turno


s1 = Signo('x')
s2 = Signo('9')

j1 = Jugador("Benjamín", s1.getSigno())
j2 = Jugador("Benjamín_Doppelganger", s2.getSigno())

tab = Tablero()

juego = Juego(j1, j2)
juego.main(tab)