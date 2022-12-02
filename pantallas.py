import pygame as pg
from figura_class import Pelota , Raqueta

ALTO = 600 # una variable en mayuscula es siempre fija
ANCHO = 800



class Partida:
    
    def __init__(self) :
        pg.init()
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Pong")
        self.tasa_refresco = pg.time.Clock()
        
        
        self.pelota = Pelota (ANCHO//2,ALTO //2,vx=2,vy=2) # ancho ,alto y velocidad
        self.raqueta1 = Raqueta(10,ALTO//2,vy = 5)
        self.raqueta2 = Raqueta (ANCHO-10,ALTO//2,vy=5)
        self.font = pg.font.Font(None, 40)


    def bucle_pantalla (self):
        game_over = False
        contador_linea1 = 0
        contador_linea2 = 50
        while not game_over:
          
            self.tasa_refresco.tick(280)#variable para controlar la velocidad entre fotogramas
   

            for evento in pg.event.get():
                
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.raqueta1.mover(pg.K_w,pg.K_s)#mover raqueta1 izquierda
            self.raqueta2.mover(pg.K_UP,pg.K_DOWN)#mover raqueta2 derecha
            self.pelota.mover()#mover pelota

            self.pantalla_principal.fill((72,156,75))#pintado de pantalla
            
            # logica para que rebote la pelota al tocar la raqueta
            self.pelota.comprobar_choque (self.raqueta1,self.raqueta2)
            self.pelota.marcador(self.pantalla_principal)#pintado de marcador
            
            contador_linea1 = 0
            contador_linea2 = 50  
            while contador_linea1 <= 560 and contador_linea2 <= 630 :
                pg.draw.line(self.pantalla_principal, (255,255,255), (400,contador_linea1), (400,contador_linea2), width=10)#pintando linea blanca
                contador_linea1 += 70
                contador_linea2 += 70
            
            self.pelota.dibujar(self.pantalla_principal)#pintado de pelota
            self.raqueta1.dibujar(self.pantalla_principal)#pintado de raqueta1
            self.raqueta2.dibujar(self.pantalla_principal)#pintado de raqueta2
            #self.mostrar_jugador()   
    def mostrar_jugador (self):
        jugador1 = self.font.render("Jugador 1",0,(255,255,0))
        jugador2 = self.font.render("Jugador 2",0,(255,255,0))
        self.pantalla_principal.blit(jugador1,(200,30))
        self.pantalla_principal.blit (jugador2,(600,30))
            
    
    pg.display.flip()
        
pg.quit    