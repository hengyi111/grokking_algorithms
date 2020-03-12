# 广度优先搜索：实现图+实现算法
from collections import deque


def my_graph():
    """实现图"""
    graph = {"you": ["alice", "bob", "claire"], "alice": ["peggy"], "bob": ["anuj"], "claire": ["thom", "jonny"],
             "peggy": [], "anuj": [], "thom": [], "jonny": []}
    # 官方写成上面形式，但是下面的形式比较直观
    # graph = {"you": ["alice", "bob", "claire"]}
    # graph["alice"] = ["peggy"]
    # graph["bob"] = ["anuj"]
    # graph["claire"] = ["thom", "jonny"]
    # graph["peggy"] = []
    # graph["anuj"] = []
    # graph["thom"] = []
    # graph["jonny"] = []
    return graph  # 需要return后才能被其他函数使用


def person_is_seller(name: str) -> bool:
    """判断是否是seller，返回bool值"""
    return name[-1] == 'm'


def search(name: str) -> str:
    """实现广度优先搜索算法"""
    graph = my_graph()  # 实现图
    search_deque = deque(graph[name])
    searched = []  # 用来记录已经被检查的人
    while search_deque:
        person = search_deque.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person, "is a seller!")
                return person
            else:
                search_deque.extend(graph[person])  # 使用extend
                searched.append(person)  # 加入到已被检查的人中
    print("No friends is seller! ")


if __name__ == "__main__":
    name0 = "you"
    name1 = "bob"
    search(name0)
    search(name1)



