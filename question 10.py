moves = input("Enter moves")
commands = [move.strip() for move in moves.split(",")]

x = 0
y = 0

for comm in commands:
    direction, steps = comm.split()
    steps = int(steps)

    if direction == "UP":
        y += steps
    elif direction == "DOWN":
        y -= steps
    elif direction == "LEFT":
        x -= steps
    elif direction == "RIGHT":
        x += steps

distance = round((x**2 + y**2)**0.5)
print(distance)
