import pygame as pg
from figura_class import Pelota,Raqueta
from utils import *



class Partida:
    def __init__(self,pantalla,refresco):
       
        self.pantalla_principal = pantalla
        self.tasa_refresco = refresco

        self.pelota = Pelota(ANCHO//2,ALTO//2,vx=2,vy=2)
        
        self.raqueta1 = Raqueta(10,ALTO//2,vy=5)
        self.raqueta1.direccion = 'izqda'
        self.raqueta2 = Raqueta(ANCHO-20,ALTO//2,vy=5)
        self.raqueta2.direccion = 'drcha'
        
        self.font = pg.font.Font("fonts/pressStart2P.ttf", 15)
        self.fuenteTemp = pg.font.Font("fonts/pressStart2P.ttf",30) 
        self.marcador1 = 0
        self.marcador2 = 0
        self.quienMarco = ""
        self.temporizador = TIEMPO_LIMITE#en milisegundos
        self.colorFondo = VERDE  
        self.contadorFotograma=0
        self.sonido = pg.mixer.Sound("songs/pelota.mp3")
        
        

    def bucle_pantalla(self):
        #reinicio de estos parametros
        self.temporizador = TIEMPO_LIMITE    
        self.marcador1 = 0
        self.marcador2 = 0
        self.tasa_refresco.tick()

        game_over = False
        while not game_over and (self.marcador1<10 or self.marcador2<10) and self.temporizador > 0:

            salto_tiempo = self.tasa_refresco.tick(FPS)#1000/280 = cantidad de fotograma por segundo pero en milisegundos
            self.temporizador -= salto_tiempo
            #print("tasa refresco: "+str(salto_tiempo) )

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True

            self.raqueta1.mover(pg.K_w,pg.K_s)
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)
            self.quienMarco = self.pelota.mover()
       
            
            self.pantalla_principal.fill(self.fijar_fondo())
           
            
            self.pelota.comprobar_choqueV2(self.raqueta2,self.raqueta1)
            self.sonido.stop()


            self.marcador()
            self.linea_disc()
          
            tiempo = self.font.render( str( int(self.temporizador/1000) ),0, ROJO)
            self.pantalla_principal.blit(tiempo, (400, 20 ))


            self.pelota.dibujar(self.pantalla_principal)
            self.raqueta1.dibujar(self.pantalla_principal)
            self.raqueta2.dibujar(self.pantalla_principal)
            self.mostrar_jugador()
            
            pg.display.flip()
        
        return self.resultado_final()

             

    def linea_disc(self):
        cont_linea1=0
        cont_linea2=50

        while cont_linea1 <= 560 and cont_linea2 <= 630:
            pg.draw.line(self.pantalla_principal, BLANCO, (400,cont_linea1), (400,cont_linea2), width=10)
            cont_linea1 += 70
            cont_linea2 += 70

    def mostrar_jugador(self):
        jugador1 = self.font.render("Jugador 1",0, AMARILLO)
        jugador2 = self.font.render( "Jugador 2",0, AMARILLO)
        self.pantalla_principal.blit(jugador1, (155, 30))
        self.pantalla_principal.blit(jugador2, (555, 30 ))

    def marcador(self):
        if self.quienMarco == "right":
            self.marcador1 += 1
        elif self.quienMarco == "left":
            self.marcador2 += 1  
        marcadorIzquierda = self.font.render(str( self.marcador2),0, AMARILLO)
        marcadorDerecha = self.font.render( str(self.marcador1),0, AMARILLO)
        self.pantalla_principal.blit(marcadorDerecha, (200, 50))
        self.pantalla_principal.blit(marcadorIzquierda, (600, 50 ))

    def fijar_fondo(self):
        self.temporizador

        self.contadorFotograma +=1

        if self.temporizador > PRIMER_AVISO:#no entra en ninguna condicion aun
            self.colorFondo=VERDE
            self.contadorFotograma=0

        elif self.temporizador > SEGUNDO_AVISO:#entra en la condicion que parpadee en naranja, 10 SEGUNDOS

            if self.contadorFotograma == 30:
                if self.colorFondo == VERDE:
                    self.colorFondo = NARANJA
                else:
                    self.colorFondo = VERDE
                self.contadorFotograma = 0
            
        else:# entra en la condicion que parpadee en rojo, 5 SEGUNDOS
            if self.contadorFotograma == 30:
                if self.colorFondo == VERDE:
                    self.colorFondo = ROJO
                else:
                    self.colorFondo = VERDE
                self.contadorFotograma = 0

        return self.colorFondo

    def resultado_final(self):
        if self.marcador1 > self.marcador2:
            return f"Gana el Jugador 2, resultado Jugador1: {self.marcador2} Jugador2: {self.marcador1}"
        elif self.marcador2 > self.marcador1:
            return f"Gana el Jugador 1, resultado Jugador1: {self.marcador2} Jugador2: {self.marcador1}"
        else:      
            return f"Empate, resultado Jugador1: {self.marcador2} Jugador2: {self.marcador1}"

class Menu:
    def __init__(self,pantalla,refresco):
        
        self.pantalla_principal = pantalla
        self.tasa_refresco = refresco

        self.imagenFondo = pg.image.load("images/portada.jpg")
        self.fuenteMenu = pg.font.Font("fonts/pressStart2P.ttf", 20)
        self.musica = pg.mixer.Sound("songs/inicio.mp3")

    def bucle_pantalla(self):

       
        self.musica.play()
       
        game_over = False
        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True

                if evento.type == pg.KEYDOWN:#pulsa enter
                    if evento.key == pg.K_RETURN:
                        #game_over = True
                        self.musica.stop()
                        return "jugar"
                    elif evento.key == pg.K_r:
                        self.musica.stop()  
                        #game_over = True
                        return "records" 

            self.pantalla_principal.blit(self.imagenFondo,(0,0))
            jugar = self.fuenteMenu.render("Pulsa ENTER para jugar",0,ROJO)
            record = self.fuenteMenu.render("Pulsa R para ver records",0,ROJO)
            self.pantalla_principal.blit(jugar, (155,ALTO//2) )
            self.pantalla_principal.blit(record, (155,ALTO//2.4) )
            pg.display.flip()
        self.musica.stop()

class Resultado:
    def __init__(self,pantalla,refresco):
        
        self.pantalla_principal = pantalla
        self.tasa_refresco = refresco

        self.fuenteResultado = pg.font.Font("fonts/pressStart2P.ttf", 12)
        self.resultado = ""

    def bucle_pantalla(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True

                if evento.type == pg.KEYDOWN:#pulsa enter
                    if evento.key == pg.K_RETURN:
                        game_over = True#con esto cierra la ventaja de resultado
                        #return "jugar"#retorna          

        
            self.pantalla_principal.fill(BLANCO)
            result = self.fuenteResultado.render(self.resultado,0,ROJO)
            self.pantalla_principal.blit(result, (135,ALTO//2) )
            pg.display.flip()

    def recibir_resultado(self,resultado):
        self.resultado = resultado



class Records:
    def __init__(self,pantalla,refresco):
      
        self.pantalla_principal = pantalla
        self.tasa_refresco = refresco
        self.fuenteResultado = pg.font.Font("fonts/pressStart2P.ttf", 12)

    def bucle_pantalla(self):
        game_over = False

        while not game_over:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    #game_over = True
                    return True

                if evento.type == pg.KEYDOWN:#pulsa enter
                    if evento.key == pg.K_RETURN:
                        game_over = True#con esto cierra la ventaja de resultado        

        
            self.pantalla_principal.fill(BLANCO)
            result = self.fuenteResultado.render("RECORDS",0,ROJO)
            self.pantalla_principal.blit(result, (135,ALTO//2) )
            pg.display.flip()
        