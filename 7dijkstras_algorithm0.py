# 狄克斯特拉算法
# graph用字典的嵌套来实现，取值方法为graph1["start"]['a'] = 6

# graph的实现，用双层索引访问索引表示的这两节点的权重值
# 写法1：
# graph = {"start": {'a': 6, 'b': 2}, 'a': {"fin": 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}

# 写法2：
graph = dict()
graph["start"] = {'a': 6, 'b': 2}
graph['a'] = {"fin": 1}
graph['b'] = {'a': 3, 'fin': 5}
graph['fin'] = {}

# 写法3：
# graph = {}
# graph["start"] = {}
# graph["start"]["a"] = 6
# graph["start"]["b"] = 2
#
# graph["a"] = {}
# graph["a"]["fin"] = 1
#
# graph["b"] = {}
# graph["b"]["a"] = 3
# graph["b"]["fin"] = 5
#
# graph["fin"] = {}

# cost开销表的实现,起点到某个节点的开销
infinity = float("inf")  # python中无穷大的表示
cost = {'a': 6, 'b': 2, "fin": infinity}

# parent父节点的实现
parent = {'a': "start", 'b': "start", "fin": None}

# 保存处理过的节点
processed = []


# 找到开销最小的节点
def find_lowest_cost_node(my_cost):
    lowest_cost = float("inf")
    lowest_cost_node = None  # 先设定用来比较的初始值
    for i in my_cost.keys():  # 不用keys默认返回的也是键
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
# 类似于打印parent["fin"],parent[parent["fin"]],parent[parent[parent["fin"]]]
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

