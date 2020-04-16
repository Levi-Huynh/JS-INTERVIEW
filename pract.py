# https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/great-graphs-afc1a343/

from util import Queue

from graph import Graph

myG = Graph()

given_v1 = 5
given_v2 = 3
given_v3 = 1

myG.add_vertex(5)
myG.add_vertex(3)
myG.add_vertex(1)
myG.add_vertex(4)
myG.add_vertex(2)

myG.add_undirected_edge(1, 2)
myG.add_undirected_edge(2, 3)
myG.add_undirected_edge(4, 5)

mynodes = [1, 3, 5]

# return neightbors path for each vertext
# return the longest path of neighbors for all vertexs


q = Queue()
# arbitrarly pick start vertex
val = mynodes.pop(0)
q.enqueue([val])

visited = set()
store_max = []
while q.size() > 0:
    path = q.dequeue()

    vert = path[-1]
    print("vert", vert, "curr_que", q)
    max1 = len(path)
    store_max.append(max1)

    if vert not in visited:
        print("vert in bft order ", vert)
        # only add the dequed vertices that are not in visited
        visited.add(vert)
    else:
        if len(mynodes) > 0:
            val = mynodes.pop()
            print("mynodes", mynodes)
            q.enqueue([val])
    for neighbor in myG.get_neighbors(vert):
        print("get", neighbor)
        if neighbor is None and len(mynodes) > 0:
            val = mynodes.pop()
            print("mynodes", mynodes)
            q.enqueue([val])
        elif neighbor is not None:
            if neighbor not in visited:
                print("neigh of ver is", neighbor, "vert", vert)

                pathCopy = path.copy()
                pathCopy.append(neighbor)
                print("pathcopy", pathCopy)
                q.enqueue(pathCopy)
                #print("q", q )
            else:
                if len(mynodes) > 0:
                    val = mynodes.pop()
                    print("mynodes", mynodes)
                    q.enqueue([val])

max_path = max(store_max)
print("max", max_path)

# return visited[mymax]
# upper

# neighbor-path == find each neighbor of last vertex, append it to prev neighbor path
# store neighbor-path len of each one as max, return max at end of traversal
