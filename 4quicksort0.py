# 递归练习
def my_sum(my_list: list):
    """递归求和"""
    if not my_list:
        return 0
    else:
        return my_list[0] + my_sum(my_list[1:])


print(my_sum([1, 2, 3, 4]))


def count_list(my_list: list):
    """计算列表中元素个数"""
    if not my_list:  # my_list == [] 可以改为if not my_list
        return 0
    else:
        return 1 + count_list(my_list[1:])


print(count_list([1, 2, 3, 4]))


def find_max(my_list: list):
    """找出列表中最大的数字"""
    if len(my_list) == 2:
        return my_list[0] if my_list[0] > my_list[1] else my_list[1]  # 注意写法
    else:
        return my_list[0] if my_list[0] > find_max(my_list[1:]) else find_max(my_list[1:])


print(find_max([1, 1112, 3, 455]))



