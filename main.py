from bricks_toolkit.screen_controller import *
from bricks_toolkit.bricks_behaviour import *

wall = BricksWall()

meshCar = [['0', '1', '0'], ['1', '1', '1'], ['0', '1', '0'], ['1', '0', '1']]
player = GameObject(Vector2(3, 16))
player.setMesh(meshCar)

road = [['1', '0', '0', '0', '0', '0', '0', '0', '0', '0'], 
        ['1', '0', '0', '0', '0', '0', '0', '0', '0', '1'], 
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '1']]
roadList = []

for x in range(0,8):
    r = GameObject(Vector2(0, (x*3) - 3))
    r.setMesh(road)
    roadList.append(r)

framerate = 1.0/10
now = time.time()
nextFramerate = now + framerate
while True:
    key = wall.win.checkKey()

    if key ==  'd' and player.position.x < 6:
        player.position.translate(Vector2(1, 0))
    if key ==  'a' and player.position.x > 1:
        player.position.translate(Vector2(-1, 0))
    for elem in roadList:
        print(elem.position)
        elem.position.translate(Vector2(0, 1))
        if elem.position.y > 19:
            elem.position.y = -4

    wall.overlap(roadList + [player])

    while now < nextFramerate:
        time.sleep(nextFramerate - now)
        now = time.time()
    nextFramerate += framerate