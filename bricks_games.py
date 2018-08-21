from bricks_toolkit.screen_controller import *
from bricks_players import *

class Topgear():
    """docstring for Topgear"""
    def __init__(self, wall):
        self.wall = wall
        self.gameplay()

    def gameplay(self):
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
        framerate = 1.0/120
        now = time.time()
        nextFramerate = now + framerate
        t= 0
        f = 0
        deltatime = framerate
        self.bech = []
        key = ''
        while key != 'r':
        #for x in range(0, 100):
            t = time.time()
            key = self.wall.win.checkKey()
            if speed > 0:
                if cont == 8:
                    rand = random.randint(0, 6)
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
                        lifes = self.die(lifes, player, roadList, carList, self.wall)
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

            self.wall.matrizOverlap(roadList + carList + [player])
            self.wall.pointWall(lifeBricks(lifes))

            while now < nextFramerate:
                time.sleep(nextFramerate - now)
                now = time.time()
            nextFramerate += framerate
            f = time.time()
            deltatime = f - t
            self.bech.append(1.0/deltatime)

    def die(self, life, p, road, cars, bricks):
        life = life - 1
        for cont in range(0, 2):
            anim = GameObject(p.position)
            anim.setMesh(dieBricks(cont))
            bricks.matrizOverlap(road + cars + [anim])
            bricks.win.redraw()
            time.sleep(0.2)
        return life

class SnakeGame():
    """docstring for SnakeGame"""
    def __init__(self, wall):
        self.wall = wall
        self.gameplay()

    def gameplay(self):
        snake = Snake()
        lifes = 4
        up = Vector2(0, -1)
        down = Vector2(0, 1)
        leaft = Vector2(1, 0)
        rigt = Vector2(-1, 0)
        velSnake = 0

        point = GameObject(randomVector2())
        point.setMesh([['1']])
        pointFrame = 0
        contFrame = 0
        framerate = 1.0/60
        now = time.time()
        nextFramerate = now + framerate
        t= 0
        f = 0
        deltatime = framerate 
        while lifes > 0:
            t = time.time()
            key = self.wall.win.checkKey()

            if key == 'a' and (snake.dir.y == -1 or snake.dir.y == 1):
                snake.dir = rigt
            elif key == 'w' and (snake.dir.x == -1 or snake.dir.x == 1):
                snake.dir = up
            elif key == 'd' and (snake.dir.y == -1 or snake.dir.y == 1):
                snake.dir = leaft
            elif key == 's' and (snake.dir.x == -1 or snake.dir.x == 1):
                snake.dir = down

            if velSnake >= 0.2:
                snake.move(point)
                velSnake = 0
            else:
                velSnake += deltatime

            if contFrame >= 0.1:
                if pointFrame < 1:
                    pointFrame += 1
                else:
                    pointFrame = 0
                contFrame = 0
            else:
                contFrame += deltatime
            point.setMesh(plot(pointFrame))

            for elem in snake.corpo:
                if elem != snake.corpo[0]:
                    if snake.corpo[0].position.x == elem.position.x and snake.corpo[0].position.y == elem.position.y:
                        lifes = self.die(lifes, snake.corpo[0], self.wall)
                        snake.create()
            if snake.corpo[0].position.x > 9 or snake.corpo[0].position.x < 0 or snake.corpo[0].position.y > 19 or snake.corpo[0].position.y < 0:
                lifes = self.die(lifes, snake.corpo[0], self.wall)
                snake.create()

            self.wall.matrizOverlap(snake.getBody() + [point])
            self.wall.pointWall(lifeBricks(lifes))

            while now < nextFramerate:
                time.sleep(nextFramerate - now)
                now = time.time()
            nextFramerate += framerate
            f = time.time()
            deltatime = f - t
    
    def die(self, life, p, bricks):
        life = life - 1
        for cont in range(0, 2):
            pos = p.position
            pos.x = pos.x - 2
            anim = GameObject(pos)
            anim.setMesh(dieBricks(cont))
            bricks.matrizOverlap([anim])
            bricks.win.redraw()
            time.sleep(0.2)
        return life