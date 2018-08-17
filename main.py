from bricks_games import *

wall = BricksWall()

def block(tam):
    if tam == 0:
        return [['1', '1'],
                ['1', '1']]
    if tam == 1:
        return [['1', '0', '0'],
                ['1', '1', '1']]
    if tam == 2:
        return [['1', '1', '1', '1']]
    if tam == 3:
        return [['1', '1', '0'],
                ['0', '1', '1']]
    if tam == 4:
        return [['0', '1', '0'],
                ['1', '1', '1']]
def randomBlock():
    mesh = block(random.randint(0, 4))
    go = GameObject(Vector2(3, 0))
    go.setMesh(mesh)
    for i in range(0, random.randint(0, 4)):
        go.fazgirar()
    return go

player = randomBlock()

nextblock = randomBlock()

solidBlocks = []

while 1:
    key = wall.win.checkKey()

    if key == 'space':
        player.fazgirar()
    elif key == 'd' and player.position.x < (10 - len(player.mesh[0])):
        player.position.translate(Vector2(1, 0))
    elif key == 'a' and player.position.x > 0:
        player.position.translate(Vector2(-1, 0))

    if player.position.y + len(player.mesh) == 20:
        solidBlocks.append(player)
        player = nextblock
        nextblock = randomBlock()



    player.position.translate(Vector2(0, 1))

    wall.overlap([player] + solidBlocks)
    wall.pointWall(nextblock.mesh)
    time.sleep(0.3)