# 动态规划，计算最大公共子串和最大公共子序列
input_word = "hish"
guess_word = "fish"

# 创建初始表格，值初始化为0
# 方法1：利用循环生成二维数组
# cell = []
# for i in range(len(guess_word)):
#     cell.append([])
#     for j in range(len(input_word)):
#         cell[i].append(0)

# 方法2：利用列表推导生成二维数组
cell = [[0]*len(input_word) for i in range(len(guess_word))]
print("初始表格：", cell)


# 最长公共子串
def longest_common_string():
    for a in range(len(guess_word)):
        for b in range(len(input_word)):
            if guess_word[a] == input_word[b]:
                if a != 0 and b != 0:  # 防止最左侧出现索引问题
                    cell[a][b] = cell[a-1][b-1] + 1
                else:
                    cell[a][b] = 1
            else:
                cell[a][b] = 0
    print("子串：", cell, max(max(cell)))


# 最长公共子序列,不适用两个单词长度不同的情况
def longest_common_sequence():
    for a in range(len(guess_word)):
        for b in range(len(input_word)):
            if guess_word[a] == input_word[b]:
                if a != 0 and b != 0:
                    cell[a][b] = cell[a - 1][b - 1] + 1
                else:
                    cell[a][b] = 1
            else:
                if a == 0 and b == 0:
                    cell[a][b] = 0
                elif a == 0 and b != 0:
                    cell[a][b] = cell[a][b-1]
                elif a != 0 and b == 0:
                    cell[a][b] = cell[a-1][b]
                else:
                    cell[a][b] = max(cell[a][b-1], cell[a-1][b])
    print("子序列：", cell, cell[len(input_word)-1][len(guess_word)-1])


longest_common_string()
longest_common_sequence()



