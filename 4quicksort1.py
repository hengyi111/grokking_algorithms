# 快速排序，用到了递归（自己调用自己，旨在缩小问题规模）的思想
def quicksort(my_array: list) -> list:
    if len(my_array) <= 1:
        return my_array  # 返回1个或0个元素的数组，停止递归的条件
    else:
        pivot = my_array[0]  # 基准值，取第一个值
        # left_part = []
        # right_part = []
        # for i in range(1, len(my_array)):
        #     if my_array[i] < pivot:
        #         left_part.append(my_array[i])
        #     else:
        #         right_part.append(my_array[i])

        # 可以直接用列表推导式,更加简洁
        left_part = [i for i in my_array[1:] if i < pivot]
        right_part = [i for i in my_array[1:] if i > pivot]
        return quicksort(left_part) + [pivot] + quicksort(right_part)


array0 = [1, 9, 5, 7, 8]  # 不能有重复数据
print(quicksort(array0))
