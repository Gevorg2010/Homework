paths = {4: (20, True, 3), 5: (10, True, 3), 6: (30, True, 2), 3: (5, False, 2), 2: (2, False, 1), 1: (0, False)}
distances = []
ways = {}

def walk(dict, start, a):
    dis = 0
    way = [a]
    while len(start) != 2:
        dis += start[0]
        way.append(start[2])
        start = dict[start[2]]
    ways.update({dis: way})
    return dis

for i, j in list(paths.items()):
    if j[1]:
        distances.append(walk(paths, j, i))

print(*ways[min(distances)])