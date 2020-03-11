# 选择排序
# 将数组中的数按从小到大的顺序排列
# 先每次找出最小数的索引，然后根据索引pop


def find_index(my_list: list) -> int:
    # 若出现双重循环，则直接将内层循环定义为函数来调用
    smallest = my_list[0]
    smallest_index = 0
    for i in range(1, len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
            smallest_index = i
    return smallest_index


def selection_sort(my_list: list) -> list:
    out_arr = []
    for i in range(len(my_list)):
        smallest = my_list.pop(find_index(my_list))
        out_arr.append(smallest)
    return out_arr


if __name__ == "__main__":
    list0 = [5, 52, -87, 2, -1]
    print(sorted(list0))  # python自带的排序，返回新的list
    print(selection_sort(list0))
