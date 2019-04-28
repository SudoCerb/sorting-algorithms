# generate random integer values
from random import shuffle

# # generate integers
# def generate(x, y):
#     # seed random number generator
#     seed(x)
#     list = []
#     for i in range(y):
#         value = randint(0, y)
#         list.append(value)
#
#     return list
#
# output  = generate(1,20)
# print(output)

def generate(x):
    l = list(range(1,x + 1))
    shuffle(l)
    return l
