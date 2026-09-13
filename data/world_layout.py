from math import pi

MAP_HALF_EXTENT = 5.0  # map spans [-5.0, 5.0] on both x and y (10m side)
MAP_RESOLUTION = 0.05
MAP_SIZE_PX = 200

WALL_THICKNESS = 0.2
WALL_HEIGHT = 1.0

GOAL = (-4.0, 4.0)

SPAWN_POINTS = [
    # bottom edge
    (-0.5, -4.0),
    (1.5, -4.0),
    (3.5, -4.0),
    # right edge 
    (4.0, -3.5),  
    (4.0, -1.5), 
    (4.0, 0.5), 
]

SPAWN_YAWS = [
    pi / 2,  # sp0 bottom -> north
    pi / 2,  # sp1 bottom -> north
    pi / 2,  # sp2 bottom -> north
    pi,      # sp3 right  -> west
    pi,      # sp4 right  -> west
    pi,      # sp5 right  -> west
]

OBSTACLE_RADIUS = 0.225 
OBSTACLE_HEIGHT = 0.5
OBSTACLE_EXCLUSION_RADIUS = 1.0 
OBSTACLE_GRID_STEP = 2.0
OBSTACLE_GRID_RANGE = (-3.0, 3.0)


def _frange(start, stop, step):
    values = []
    v = start
    while v <= stop + 1e-9:
        values.append(round(v, 3))
        v += step
    return values


def generate_obstacle_grid():
    coords = _frange(OBSTACLE_GRID_RANGE[0], OBSTACLE_GRID_RANGE[1], OBSTACLE_GRID_STEP)
    excluded_points = [GOAL] + SPAWN_POINTS

    obstacles = []
    for x in coords:
        for y in coords:
            too_close = any(
                ((x - ex) ** 2 + (y - ey) ** 2) ** 0.5 < OBSTACLE_EXCLUSION_RADIUS
                for ex, ey in excluded_points
            )
            if not too_close:
                obstacles.append((x, y))
    return obstacles


OBSTACLES = generate_obstacle_grid()
