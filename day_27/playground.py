# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
    
    
# print(add(1,2,3.78,89,33,65))


def calculate(n, **kw):
    n += kw.get("add")
    n *= kw.get("multiply")
    print(n)
    
calculate(3, add = 5)    