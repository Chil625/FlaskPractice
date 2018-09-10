def methodception(another):
    return another()


def add_two_numbers():
    return 36 + 75


# print(methodception(add_two_numbers))

# print(methodception(lambda: 36 + 75))

my_list = [13, 56, 77, 484]
print(list(filter(lambda x: x != 13, my_list)))

# (lambda x: x * 3)(5)


# def f(x):
#     return x * 3


def not_thirteen(x):
    return x != 13


print(list(filter(not_thirteen, my_list)))
# f(5)
