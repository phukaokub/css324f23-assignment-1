def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s == (4, 4, 0)

def successors(s):
    x, y, z = s
    if x > 0:
        # Pour water from x to y
        yield ((x - min(x, 5 - y), y + min(x, 5 - y), z), 1)  # Change cost to 1 (integer)
        # Pour water from x to z
        yield ((x - min(x, 3 - z), y, z + min(x, 3 - z)), 1)  # Change cost to 1 (integer)
    if y > 0:
        # Pour water from y to x
        yield ((x + min(y, 8 - x), y - min(y, 8 - x), z), 1)  # Change cost to 1 (integer)
        # Pour water from y to z
        yield ((x, y - min(y, 3 - z), z + min(y, 3 - z)), 1)  # Change cost to 1 (integer)
    if z > 0:
        # Pour water from z to x
        yield ((x + min(z, 8 - x), y, z - min(z, 8 - x)), 1)  # Change cost to 1 (integer)
        # Pour water from z to y
        yield ((x, y + min(z, 5 - y), z - min(z, 5 - y)), 1)  # Change cost to 1 (integer)