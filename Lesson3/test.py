def sumNum(*agrs):
    return sum(agrs)
print(sumNum(1,2,3))

def sumNum1(lst):
    return sum(lst)
print(sumNum1([1,2,3,4]))

def stulist(*args, **kwargs):
    str=""
    for k, v in kwargs.items():
        str += k + v + "\n"
    return str

print(stulist(1,2,3,Name=": Sophea",Sex=": Male"))