def sumNum(*agrs):
    return sum(agrs)

def sumNum1(lst):
    return sum(lst)

def stulist(*args, **kwargs):
    str=""
    for k, v in kwargs.items():
        str += k + v + "\n"
    return str
