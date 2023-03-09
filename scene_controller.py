from pantallas import *
from utils import  ANCHO,ALTO


class SceneController:
    def __init__(self):
        self.pantalla_principal = pg.display.set_mode((ANCHO,ALTO))
        pg.display.set_caption("Pong")
        self.tasa_refresco = pg.time.Clock()

        #para agregar records o mejores puntajes
        self.puntajes={
            'jugador1':['12/12/22','10 goles','1'],
            'jugador1':['12/12/22','10 goles','2'],
        }

        #self.menu = Menu(self.pantalla_principal,self.tasa_refresco)
        #self.resultado = Resultado(self.pantalla_principal,self.tasa_refresco)
        #self.partida = Partida(self.pantalla_principal,self.tasa_refresco)
        #self.records = Records(self.pantalla_principal,self.tasa_refresco)

        self.pantallas = [ Menu(self.pantalla_principal,self.tasa_refresco),Partida(self.pantalla_principal,self.tasa_refresco),Resultado(self.pantalla_principal,self.tasa_refresco),Records(self.pantalla_principal,self.tasa_refresco) ]

        self.valor_resultado=""
        #tarea mejorar codigo de while dentro del metodo start
        



    def start(self):
        seguir = True    

        indice = 0
        while seguir:
           if indice == 1: 
                cerrar = self.valor_resultado = self.pantallas[indice].bucle_pantalla()
                print("estoy en partida",str(indice))
                if cerrar == True:
                    break
                indice +=1

           elif indice == 2:
                self.pantallas[indice].recibir_resultado(self.valor_resultado)
                cerrar = self.pantallas[indice].bucle_pantalla()
                if cerrar == True:
                    break
                print("estoy en resultado",str(indice))
                indice = 0 
                
           elif indice == 0:
                cerrar = self.pantallas[indice].bucle_pantalla()
                #print("esto es menu",cerrar)
                if cerrar == 'records':
                    self.pantallas[3].bucle_pantalla()
                if cerrar == True:
                    break
                print("estoy en menu",str(indice))
                indice +=1


           

              
                

        '''
            cerrar = self.menu.bucle_pantalla()
            if cerrar == True:
                break
            cerrar = self.valor_resultado = self.partida.bucle_fotograma()
            if cerrar == True:
                break
            self.resultado.recibir_resultado(self.valor_resultado)
            cerrar = self.resultado.bucle_pantalla()
            if cerrar == True:
                break
        '''

           

