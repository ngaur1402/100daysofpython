#https://reeborg.ca/reeborg.html : Maze


def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear() == "TRUE":
        turn_right()
        move()
    elif front_is_clear() == "TRUE":
        move()
    else:
        turn_left()
