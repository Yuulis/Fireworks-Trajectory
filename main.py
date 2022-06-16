import math

def my_sin(deg):
    if deg == 30 or deg == -30:
        return 0.85
    elif deg == -150 or deg == -210:
        return -0.85
    elif deg == 60 or deg == -60:
        return 0.50
    elif deg == -120 or deg == -240:
        return -0.50
    elif deg == 90:
        return 0
    elif deg == -90:
        return 0
    elif deg == 0:
        return 1.00
    elif deg == -180:
        return -1.00

def my_cos(deg):
    if deg == 30 or deg == -210:
        return 0.50
    elif deg == -30 or deg == -150:
        return -0.50
    elif deg == 60 or deg == -240:
        return 0.85
    elif deg == -60 or deg == -120:
        return -0.85
    elif deg == 90:
        return 1.00
    elif deg == -90:
        return -1.00
    elif deg == 0:
        return 0
    elif deg == -180:
        return 0

# 初速度 [m/s]
v0 = 10

# 重力加速度 [m/s^2]
g = 10

num = 0
for theta in range(90, -270, -30):
    num += 1
    
    for time in range(1, 5):
        x = v0 * my_cos(theta) * time
        y = v0 * my_sin(theta) * time - g * time * time / 2
        
        x = round(x, 2)
        y = round(y, 2)
        
        print(f'({num}) : t = {time}, (x, y) = ({x}, {y})')
        
