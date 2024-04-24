#Llibrerias del programa
import time
from os import system
import keyboard

#Funciones del programa
def vacaDefinicion():
    from cowsay import cowsay
    message = """
    |--------------------------------------|
    |---| Aqui sera la definiciones |----|
    |--------------------------------------|
    """.strip()
    print(cowsay(message))

from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen

def intro():
    def demo(screen):
        effects = [
            Cycle(
                screen,
                FigletText("|||-> EL  Llibre  de  les  Accepcions <-|||", font='big'),
                int(screen.height / 2 - 8)),
            Stars(screen, 100)
        ]
        screen.play([Scene(effects, 200)])

    Screen.wrapper(demo)

intro()
time.sleep(3)

print("Presiona cualquier tecla para continuar...")
keyboard.wait('any')

# Limpia la pantalla
system("cls")

print("HOLA ISRADURNE")


