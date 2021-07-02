
# aim of prim's alg0 :find the minimum cost span tree

mat = [] # adjacency matrix

mat.append([0,3,0,0,6,5]) #for a
mat.append([3,0,1,0,0,4])#b
mat.append([0,1,0,6,0,4])#c
mat.append([0,0,6,0,8,5])#d
mat.append([6,0,0,8,0,2])#e
mat.append([5,4,4,5,2,0])#f
for i in range(len(mat)):
    for j in range(len(mat)):
        if mat[i][j] == 0:
            mat[i][j] = float('inf')


visited = set()
nodes = [(index,value,0) for (index,value) in list(enumerate(mat[0]))]
nodes = (sorted(nodes,key = lambda tup : tup[1]))
print(nodes)


def update():
    global nodes
    global visited
    for i in range(len(nodes)):
        (node,value,connect) = nodes[i]
        for v in visited:
            if mat[v][node] < value and node not in visited:
                value = mat[v][node]
                connect = v
                # else:
                    # value = float("inf")
        nodes[i] = (node,value,connect)
    nodes = sorted(nodes,key = lambda tup : tup[1])

def makeinf(node):
    global nodes
    for i in range(len(nodes)):
        (a,_,v) = nodes[i]
        if a == node:
            nodes[i] = (node,float('inf'),v)


tree = []
printt = [[] for _ in range(len(mat))]
while(nodes[0][1] != float("inf")):
    a = nodes[0]
    printt[a[2]].append(a[0])
    tree.append(a)
    visited.add(a[0])
    makeinf(a[0])
    update()
    print(nodes)


re = []
for (a,b,c) in tree:
    aa = chr(97 + a)
    cc = chr(97 + c)
    re.append((aa,b,cc))
print(re)
