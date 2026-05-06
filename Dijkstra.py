graph = [("A", ("C", "F"), [3, 2]), ("C", ("D", "E", "F"), [4, 1, 2]), ("F", ("C", "E", "B", "G"), [2, 3, 6, 5]), ("E", ("B"), [2]), ("D", ("B"), [1]), ("G", ("B"), [2])]
visited = []
estimated = {}
road = [graph[0][0]]

def estimate(arr, ind, dist):
    dists = []
    for i in range(len(arr[ind][2])):
        if arr[ind][1][i] in estimated:
            if dist + i < estimated[arr[ind][1][i]]:
               dists.append(arr[ind][1][i])
               dists.append(dist + i)
        else:
            estimated.update({arr[ind][1][i]: dist + arr[ind][2][i]})
    return dists

for town in range(len(graph)):
    curr = []
    next_towns = graph[town][1]

    for next in range(len(next_towns)):
        destination = graph[town][1][next]
        passed_dis = graph[town][2][next]

        for dist in range(len(graph)):
            next_town = graph[dist][0]

            if next_town == destination:
                curr = estimate(graph, dist, passed_dis)
                print(curr)
                print(estimated)
                break

    visited.append(graph[town][0])

