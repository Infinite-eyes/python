#return
# def squre(n):
#     ls = [i * i for i in range(n)]
#     return ls
#
#
# for i in squre(5):
#     print(i, end='  ')

# yield
def squre(n):
    for i in range(n):
        yield i * i


for i in squre(5):
    print(i, end='  ')
