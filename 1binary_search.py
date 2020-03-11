import math


def binary_search(my_list: list, my_num: int):
    """
    二分查找
    接受一个有序数组和一个数，如果该数存在于数组中，返回其索引位置
    """
    low_index = 0
    high_index = len(my_list) - 1
    if my_list[low_index] < my_list[high_index]:  # 说明列表元素升序排列
        while low_index <= high_index:
            mid_index = math.floor((low_index + high_index) / 2)
            mid_num = my_list[mid_index]  # 中间索引值对应的数
            if my_num > mid_num:
                low_index = mid_index + 1
            elif my_num < mid_num:
                high_index = mid_index - 1
            elif my_num == mid_num:
                return mid_index
        return None  # 循环到低索引大于高索引，则说明不存在该数
    else:  # 列表元素降序排列
        while low_index <= high_index:
            mid_index = math.floor((low_index + high_index) / 2)
            mid_num = my_list[mid_index]  # 中间索引值对应的数
            if my_num > mid_num:
                high_index = mid_index - 1
            elif my_num < mid_num:
                low_index = mid_index + 1
            elif my_num == mid_num:
                return mid_index
        return None  # 循环到低索引大于高索引，则说明不存在该数


if __name__ == "__main__":
    list0 = [1, 2, 3, 4, 5]
    list1 = list0[:]
    list1.reverse()
    num0 = 2
    print(binary_search(list0, num0))  # 升序数组
    print(binary_search(list1, num0))  # 降序数组
