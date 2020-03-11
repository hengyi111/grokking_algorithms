# recursion 递归
def countdown(n):
    if n == 0:
        return 0  # 停止调用
    else:
        print(n, end=' ')
        return countdown(n-1)  # 调用自己


def greet2(name):
    print("how are you,", name, "?")


def bye():
    print("bye")


def greet(name):
    print("hello,", name)
    greet2(name)
    print("below is bye")
    bye()


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


countdown(10)  # 倒计数
greet("ciri")
print(factorial(5))