# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
    
    
# print(add(1,2,3.78,89,33,65))


# def calculate(n, **kw):
#     n += kw.get("add")
#     n *= kw.get("multiply")
#     print(n)
    
# calculate(3, add = 5, multiply = 3)  


class Car:
    
    def __init__(self, **kw):
        self.color = kw.get("color") 
        self.door = kw.get("door") 
        self.type = kw.get("type") 
        self.brand = kw.get("brand") 
        self.model = kw.get("model")
        
my_car = Car(color = "White", door = 5, type = "Hatch back", brand = "BMW", model = "320i")
print(my_car.brand)          