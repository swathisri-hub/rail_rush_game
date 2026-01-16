WIDTH = 400
HEIGHT = 500
LANES = [100, 200, 300]

def check_collision(player, obstacle):
    ox1, oy1, ox2, oy2 = obstacle
    px1, py1, px2, py2 = player
    return ox1 < px2 and ox2 > px1 and oy1 < py2 and oy2 > py1
