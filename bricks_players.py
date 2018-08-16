from bricks_toolkit.bricks_behaviour import *
import copy
class Snake():
    """docstring for snake"""
    def __init__(self):
        self.corpo = []
        self.dir = Vector2(1, 0)
        self.create()

    def create(self):
        x = 4
        self.corpo = []
        self.dir = Vector2(1, 0)
        for i in range(0,1):
            bk = GameObject(Vector2(x - i, 3))
            bk.setMesh([['1']])
            self.corpo.append(bk)

    def getBody(self):
        return self.corpo

    def add(self, point):
        npos = self.corpo[-1].position
        self.move(point)
        bk = GameObject(npos)
        bk.setMesh([['1']])
        self.corpo.append(bk)

    def move(self, point):
        pos1 = copy.copy(self.corpo[0].position)
        pos1.translate(self.dir)
        npos = []
        npos.append(pos1)
        for id, elem in enumerate(self.corpo):
            if id > 0:
                npos.append(self.corpo[id - 1].position)

        for x, y in enumerate(npos):
            self.corpo[x].position = y

        if self.corpo[0].position.x == point.position.x and self.corpo[0].position.y == point.position.y:
            point.position = randomVector2(self.corpo)
            self.add(point)