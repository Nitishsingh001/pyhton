# 📌 Day 9: Functional Programming & Decorators
# Topics:

# map(), filter(), reduce()

# Closures & Decorators (@decorator)

# Generators (yield keyword)

# *args & **kwargs



# map()

# using two parameters one is function and other is iterable 


# numbers= [1,2,3,4,5]


# def square(x):
#     return x*x

# squared_numbers = list(map(square, numbers))
# print(squared_numbers)

# # using lambda function 

# squared_numbers_lambda = list(map(lambda x: x*x, numbers))
# print(squared_numbers_lambda)

# numbers = [1, 2, 3, 4, 5, 6]

# def is_even(x):
#     return x % 2 == 0

# evens = list(filter(is_even, numbers))
# print(evens)


from functools import reduce

numbers = [1, 2, 3, 4]

def multiply(x, y):
    return x * y

result = reduce(multiply, numbers)
print(result)
