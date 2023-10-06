def hash(func):
    def wrapper():
        print("#"*10)
        func()
        print("#"*10)
    return wrapper

def star(func):
    def inner():
        print("*"*10)
        func()
        print("*"*10)
    return inner

def percentage(func):
    def second():
        print("%"*10)
        func()
        print("%"*10)
    return second
# @star
# @percentage
# @hash

def hello():
    # print("#"*10)
    print('hello') 


# @hash
def world():
    print("world")

#same as above__ Concept of @
world=star(hash(percentage(world)))     
world()