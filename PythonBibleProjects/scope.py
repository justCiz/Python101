# using global variables in functions
a = 27

def f1():
    print(a)

def f2():
    a = 5 #local variable
    print(a)

def f3():
    global a
    a = 100 #global variable
    print(a)

f1()
f2()
print(a) #prints 27, the original value of a
f3()
print(a)


# List has exceptions for using global variables, it can be change even without using global keyword
aList = [1,2,3]

def f1List():
    aList = 1
    print(aList)

def f2List():
    aList[0] = 5
    print(aList)

print(aList)
f1List()
f2List()



def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))


# packing 
print(1,2,3,4,5)
print([1,2,3,4,5])
print(*[1,2,3,4,5])

def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(add(1,2,3,4,5))


def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
    return sentence
dictionary = {"name": "John", "age": 23, "likes": "Python"}
print(about(**dictionary))



# unpacking
def foo(**test):
    for key, value in test.items():
        print("{}:{}".format(key, value))

foo(Sex="Male", age=23, likes="Python")