import pygame as pg

class Pelota:
    def __init__(self,pos_x,pos_y,radio=20,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y =pos_y 
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy
        self.contadorDerecha = 0
        self.contadorIzquierda = 0
        self.font = pg.font.Font(None, 40)


    def dibujar(self,pantalla):
        pg.draw.circle(pantalla,self.color,(self.pos_x,self.pos_y),self.radio)

    def mover(self,y_max=600,x_max=800):
        self.pos_x += self.vx
        self.pos_y += self.vy

        if self.pos_y >= y_max-self.radio or self.pos_y < 0+self.radio:#para que rebote arriba y abajo
            self.vy *= -1 
            
            # con esto contamos los goles
        if self.pos_x >= x_max+self.radio*10:#limite derecho
            self.contadorIzquierda += 1 

            self.pos_x = x_max//2 # esto es para que la pelota aparezca en el centro al marcar gol
            self.pos_y = y_max//2
            self.vx *= -1
            self.vy *= -1 
             

        if self.pos_x < 0-self.radio*10:#limite izquierdo
            self.contadorDerecha +=1

            self.pos_x = x_max//2
            self.pos_y = y_max//2
            self.vx *= -1
            self.vy *= -1
    
    def marcador(self,pantalla_principal):
        marcadorIzquierda = self.font.render(str( self.contadorDerecha),0, (255,255,0))
        marcadorDerecha = self.font.render( str(self.contadorIzquierda),0, (255,255,0))
        pantalla_principal.blit(marcadorDerecha, (200, 50))
        pantalla_principal.blit(marcadorIzquierda, (600, 50 ))
    

    @property # esto convierte una funcion en una variable
    def derecha(self):
        return self.pos_x + self.radio
    @property
    def izquierda(self):
        return self.pos_x - self.radio
    @property
    def arriba(self):
        return self.pos_y - self.radio
    @property
    def abajo(self):
        return self.pos_y + self.radio                

    

    def comprobar_choque(self,*raquetas): # esta funcion me sirve para las 2 raquetas va con * e itera con for
        for r in raquetas:
            if self.derecha  >= r.izquierda and \
               self.izquierda  <= r.derecha and \
               self.abajo >= r.arriba and\
               self.arriba <= r.abajo:
                    self.vx *= -1
                    return # este return vacio es igual que break
   


              
    

            




class Raqueta:
    def __init__(self,pos_x,pos_y,w=20,h=100,color=(255,255,255),vx=1,vy=1):
        self.pos_x = pos_x
        self.pos_y =pos_y 
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibujar(self,pantalla):
        pg.draw.rect(pantalla,self.color,(self.pos_x-(self.w//2),self.pos_y-(self.h//2),self.w,self.h))    
        

    def mover(self,tecla_arriba,tecla_abajo,y_max=600,y_min=0):
        estado_teclas = pg.key.get_pressed()
       
        if estado_teclas[tecla_arriba] == True and self.pos_y > (y_min+self.h//2):
            self.pos_y -= 1
        if estado_teclas[tecla_abajo] == True and self.pos_y < (y_max-self.h//2) :
            self.pos_y += 1     

    @property
    def arriba(self):
        return self.pos_y - self.h//2

    @property
    def abajo(self):
        return self.pos_y + self.h//2
    
    @property
    def izquierda(self):
        return self.pos_x - self.w//2
    
    @property
    def derecha(self):
        return self.pos_x + self.w//2    
