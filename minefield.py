import random

w, h, mines = 5, 3, 3

# nastaví každé pole na nulu
field = [[0 for y in range(h)] for x in range(w)]

# put mine on random position

if mines > w * h:
    mines = 0
    print("Error: Too many mines.")
for i in range(mines):
    while True:
        
        rx = random.randint(0, w - 1)
        ry = random.randint(0, h - 1)
        if field[rx][ry] != "M":
            field[rx][ry] = "M"
            break
delta = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
for y in range(h):
    for x in range(w):
        if field[x][y] == "M": 
             print("mina je na", x,y)
           nx = x-1 
           ny = x-1
           if ny >= 0 and nx>= 0 and field[nx][ny]!="M":
                field[nx][ny] += 1
            nx = x-1 
            ny = x-1
            if ny >= 0 and nx>= 0 and field[nx][ny]!="M":
                field[nx][ny] += 1



# print field
for y in range(h):
    for x in range(w):
        print(field[x][y], end="")
    print()  
