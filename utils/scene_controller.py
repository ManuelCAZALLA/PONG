from pantallas import *

class SceneController :
    def __init__(self) :
          self.menu = Menu ()
          self.partida = Partida ()
          self.resultado = Resultado ()
          self.records = Records ()
          self.valor_resultado = ""
          
    def start (self):
        seguir = True
        while seguir :
         cerrar = self.menu.buclePantalla()
         
         self.valor_resultado = self.partida.bucle_fotograma()
         self.resultado = self.recibir_resultado (self.valor_resultado)
         cerrar = 