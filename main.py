def get_coordinate(x, y, facing):
    if facing is 'N':
        y+= 1
    elif facing is 'S':
        y-= 1
    elif facing is 'E':
        x+= 1
    elif facing is 'W':
        x-= 1
    else:
        raise Exception('Invalid Facing')
    if x < 0 or y < 0:
        raise Exception('Exceeded Boundaries')
    return x, y

def get_facing(command, facing):
    if facing is 'N':
        facing = 'E' if command is 'R' else 'W'
    elif facing is 'S':
        facing = 'W' if command is 'R' else 'E'
    elif facing is 'E':
        facing = 'S' if command is 'R' else 'N'
    elif facing is 'W':
        facing = 'N' if command is 'R' else 'S'
    else:
        raise Exceeded('Invalid Facing')
    return facing

def get_position(command, position):
    x, y, facing = position
    if command is 'M':
        x, y = get_coordinate(x, y, facing)
    elif command in ['R', 'L']:
        facing = get_facing(command, facing)
    else:
        raise Exception('Invalid Command')
    return x, y, facing

def move(commands, position):
    if len(commands) is 0:
        return position
    position = get_position(commands[0], position)
    return move(commands[1:], position)

starting = (0, 0, 'E')
commands = ['M', 'M', 'L', 'M', 'M']

print(move(commands, starting))