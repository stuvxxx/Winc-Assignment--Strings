# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line


from turtle import position


def greet(name): 
    return "Hello, " + name + "!"
print(greet("Bob"))

def add(x, y, z): 
    return x + y + z
print(add(1.2, 3, 6))    

def positive(number): 
    return number > 0
print(positive(-8))

def negative(number): 
    return number < 0
print(negative(-8))
