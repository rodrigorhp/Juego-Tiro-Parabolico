#Luis Angel Mendoza Castillón A00827838
#Rodrigo Rene Henriquez Paguaga A00827198

#Importar librerias 
from random import randrange
from turtle import *
from freegames import vector

#Inicializa las variables de la bola, su velocidad y los objetivos
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

#Recibe las cordenadas del click y asigna la velocidad a la bola
def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 10
        speed.y = (y + 200) / 10

#Recibe coordenadas del objeto y revisa si esta dentro del juego
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

#Crea los graficos de los objetos del juego
def draw():
    "Draw ball and targets."
    clear()

    #Crea todos los objetivos
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    #Crea la bola 
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

#
def move():
    "Move ball and targets."
    #Crea los objetivos aleatoriamente
    if randrange(40) == 0:
        #Asigna una altura aleatoria
        y = randrange(-150, 150)
        #Le asigna su posicion
        target = vector(200, y)
        targets.append(target)

    #Actuliza la posicion de los objetivos
    for target in targets:
        target.x -= 6

    #Revisa que la bola este en el juego y actualiza su posicion
    if inside(ball):
        speed.y -= 0.80
        ball.move(speed)

    #Crea una copia de todos los objetivos
    dupe = targets.copy()
    targets.clear()

    #Checa si la bola esta tocando un objetivo y crea la lista de los objetivos validos
    for target in dupe:
        #Reposiciona los objeetivos que el usuario no logre disparar
        if not inside(target):
            y = randrange(-150, 150)
            #Le asigna su posicion
            target = vector(200, y)
            targets.append(target)   
        if abs(target - ball) > 13:
            targets.append(target)

    #Dibuja los objetos
    draw() 

    #Velocidad del juego
    ontimer(move, 50)

#Crea la ventana del juego
setup(420, 420, 370, 0)
#Esconde el cursor
hideturtle()
up()
#Crea los dibujos sin trazarlos
tracer(False)
#Regstra los clicks en el juego
onscreenclick(tap)
#Manda a llamar la funcion para mover los objetos
move()
#Loop del juego
done()