# 狄克斯特拉算法练习
# 计算最小开销，对应书上练习7.1A

# 写法2：
graph = dict()
graph["start"] = {'a': 5, 'b': 2}
graph['a'] = {'c': 4, 'd': 2}
graph['b'] = {'a': 8, 'd': 7}
graph['c'] = {'d': 6, "fin": 3}
graph['d'] = {"fin": 1}
graph['fin'] = {}


# cost开销表的实现,起点到某个节点的开销
infinity = float("inf")
cost = {'a': 5, 'b': 2, 'c': infinity, 'd': infinity, "fin": infinity}

# parent父节点的实现
parent = {'a': "start", 'b': "start", 'c': None, 'd': None, "fin": None}

# 保存处理过的节点
processed = []


# 找到开销最小的节点
def find_lowest_cost_node(my_cost):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for i in my_cost:  # 默认返回的是键
        out_cost = my_cost[i]
        if out_cost < lowest_cost and i not in processed:
            lowest_cost = out_cost
            lowest_cost_node = i
    return lowest_cost_node


# 狄克斯特拉算法实现
node = find_lowest_cost_node(cost)
while node:
    node_cost = cost[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = node_cost + neighbors[n]
        if new_cost < cost[n]:
            cost[n] = new_cost
            parent[n] = node
    processed.append(node)
    node = find_lowest_cost_node(cost)


# 打印出最小开销的路径
path = []
out = parent["fin"]
while out != "start":
    path.append(out)
    out = parent[out]
path = ["start"] + path[::-1] + ["fin"]
print("Path of the lowest cost: ", "-->".join(path))


# 打印起点到各个节点的最小开销
print("Cost from the start to each node: ", cost)
print("Lowest cost", cost["fin"])