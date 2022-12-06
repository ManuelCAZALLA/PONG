from pantallas import Partida, Menu

#juego = Partida()# creamos objeto de la clase Partida

#juego.bucle_fotograma() # llamamos al bucle de pantalla

menu = Menu()
mensaje = menu.buclePantalla()

if mensaje == "jugar" :
    juego = Partida ()
    juego.bucle_fotograma ()



