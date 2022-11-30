from figura_class import Pelota,Raqueta
import pygame as pg

pg.init()

pantalla_principal = pg.display.set_mode((800,600))
pg.display.set_caption("Pong")

#definir la tasa de refresco de nuestro bucle de fotogramas fps= fotograma por segundo
cronometro = pg.time.Clock()

#objetos pelota y raqueta
pelota = Pelota(400,300) # no le paso los demas valores por que los coge por defecto
raqueta1 = Raqueta(10,300) # al estar definidos en la clase los demas los coge por defecto
raqueta2 = Raqueta(790,300)

#asignando velocidad
raqueta1.vy=5
pelota.vx=4


game_over = False
while not game_over:
    
    vt = cronometro.tick(60)#variable para controlar la velocidad entre fotogramas
    #print(vt)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    raqueta1.mover(pg.K_w,pg.K_s)#mover raqueta1 izquierda
    raqueta2.mover(pg.K_UP,pg.K_DOWN)#mover raqueta2 derecha
    pelota.mover()#mover pelota

    pantalla_principal.fill((72,156,75))#pintado de pantalla
 
    pelota.marcador(pantalla_principal)#pintado de marcador
    pg.draw.line(pantalla_principal, (255,255,255), (400,0), (400,600), width=2)#pintando linea blanca
    pelota.dibujar(pantalla_principal)#pintado de pelota
    raqueta1.dibujar(pantalla_principal)#pintado de raqueta1
    raqueta2.dibujar(pantalla_principal)#pintado de raqueta2
    

    pg.display.flip()