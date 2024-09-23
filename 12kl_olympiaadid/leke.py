from collections import deque

'''
    el = []
    output = []
    x = int(input())
    for i in range(x):
        el.append([p for p in input().split(' ')])
    damaged = [int(j) for j in input().split(' ')]

    for bs in el:
        try:
            if abs(int(damaged[0]) - int(bs[0])) == 1 and bs[3] == "X+" or bs[3] == "X-":
                output.append(bs[0:3])
            elif abs(int(damaged[1]) - int(bs[1])) == 1 and bs[3] == "Y+" or bs[3] == "Y-":
                output.append(bs[0:3])
            elif abs(int(damaged[2]) - int(bs[2])) == 1 and bs[3] == "Z+" or bs[3] == "Z-":
                output.append(bs[0:3])
        except:
            print("kys")

    for x in output:
        return ' '.join(x)
    '''



def find_leaky_rooms(N, rooms_with_doors, leaky_room):
    # Create a 3D grid to represent the space shuttle
    grid = [[[set() for _ in range(26)] for _ in range(26)] for _ in range(26)]
    
    # Fill the grid with the given open doors
    for x, y, z, door in rooms_with_doors:
        grid[x][y][z].add(door)

    # BFS to find all connected rooms
    queue = deque([leaky_room])
    visited = set()
    leaky_rooms = []

    while queue:
        x, y, z = queue.popleft()
        if (x, y, z) in visited:
            continue
        visited.add((x, y, z))
        leaky_rooms.append((x, y, z))

        # Check all possible directions
        directions = [('X+', 'X-', (x+1, y, z)), ('X-', 'X+', (x-1, y, z)),
                      ('Y+', 'Y-', (x, y+1, z)), ('Y-', 'Y+', (x, y-1, z)),
                      ('Z+', 'Z-', (x, y, z+1)), ('Z-', 'Z+', (x, y, z-1))]

        for door_current, door_next, (nx, ny, nz) in directions:
            if 1 <= nx <= 25 and 1 <= ny <= 25 and 1 <= nz <= 25:
                if (x, y, z) == leaky_room or (door_current in grid[x][y][z] and door_next in grid[nx][ny][nz]):
                    queue.append((nx, ny, nz))

    return leaky_rooms

# Read input
N = int(input())
rooms_with_doors = []
for _ in range(N):
    x, y, z, door = input().split()
    rooms_with_doors.append((int(x), int(y), int(z), door))

Qx, Qy, Qz = map(int, input().split())
leaky_room = (Qx, Qy, Qz)

# Find and print leaky rooms
leaky_rooms = find_leaky_rooms(N, rooms_with_doors, leaky_room)
for room in leaky_rooms:
    print(f"{room[0]} {room[1]} {room[2]}")