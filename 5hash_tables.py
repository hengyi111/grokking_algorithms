# 散列表 hash table 哈希表
# python中的hash table使用字典实现

book = {"apple": 0.5, "banana": 1.2, "milk": 5.5}
print(book)

voted = dict()


# 使用散列表检查重复
def check_voter(name: str):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote")


check_voter("bob")
check_voter("mike")
check_voter("bob")


