from bricks_toolkit.screen_controller import *
from bricks_toolkit.bricks_behaviour import *
import random

def die(life, p, road, cars, bricks):
    print('morte')
    life = life - 1
    for cont in range(0, 2):
        anim = GameObject(p.position)
        anim.setMesh(dieBricks(cont))
        bricks.overlap(road + cars + [anim])
        bricks.win.redraw()
        time.sleep(0.2)
    return life

wall = BricksWall()

meshCar = [['0', '1', '0'], ['1', '1', '1'], ['0', '1', '0'], ['1', '0', '1']]
carList = []
player = GameObject(Vector2(2, 16))
player.setMesh(meshCar)

road = [['1', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1'], 
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1']]
roadList = []
cont = 0
lifes = 4

for x in range(0,8):
    r = GameObject(Vector2(0, (x*3) - 3))
    r.setMesh(road)
    roadList.append(r)
speed = 0

framerate = 1.0/60
now = time.time()
nextFramerate = now + framerate
t= 0
f = 0
deltatime = framerate 
while lifes > 0:
    t = time.time()
    key = wall.win.checkKey()
    if speed > 0:
        if cont == 8:
            rand = random.randint(0, 2)
            if rand == 1:
                car = GameObject(Vector2(2, -4))
                car.setMesh(meshCar)
                carList.append(car)
            if rand == 2:
                car = GameObject(Vector2(5, -4))
                car.setMesh(meshCar)
                carList.append(car)
            cont = 0
        else:
            cont += 1

        for elem in roadList:
            elem.position.translate(Vector2(0, 1))
            if elem.position.y > 19:
                elem.position.y = -4

        for elem in carList:
            elem.position.translate(Vector2(0, 1))
            if player.position.y - elem.position.y == 3 and player.position.x == elem.position.x:
                lifes = die(lifes, player, roadList, carList, wall)
                carList.remove(elem)
            if elem.position.y > 19:
                carList.remove(elem)
        speed = 0
    else:
        speed += deltatime;


    if key ==  'd' and player.position.x < 6:
        player.position = Vector2(5, 16)
    if key ==  'a' and player.position.x > 1:
        player.position = Vector2(2, 16)

    wall.overlap(roadList + carList + [player])
    wall.pointWall(lifeBricks(lifes))

    while now < nextFramerate:
        time.sleep(nextFramerate - now)
        now = time.time()
    nextFramerate += framerate
    f = time.time()
    deltatime = f - t
    print(1.0/deltatime)