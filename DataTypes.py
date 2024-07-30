# Octal
print(0o123)

# Hexadecimal
print(0x123)

# exponentiation
print(1.23e4)

# Python always chooses the more economical form of the number's presentation, and you should take this into consideration when creating literals.
print(0.0000000000000000000001)

print(True > False)
print(True < False)

listTest = [1, "A", 3, True, 5]
print(listTest)
print(listTest[4:])
print(listTest[:3])
print(listTest[:5:2])
del listTest[3]
print(listTest)

listTable = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listTable)
print(listTable[1])
print(listTable[1][1])
print(listTable[1][1:])

#Tuple - can't be changed/altered once created
tupleTest = (1, "A", 3, True, 5)
print(tupleTest)
print(tupleTest[4:])
print(tupleTest[:3])
print(tupleTest[:5:2])

#Dictionaries
# keys must be unique and in the form of strings, numbers, or tuples
dictTest = {
    "key1": 1,
    "key2": "A",
    "key3": 3,
    "key4": True,
    "key5": 5
}
print(dictTest)
print(dictTest["key4"])
del dictTest["key4"]
print(dictTest)

dictTest2 = {1: "A", 2: "B", 3: "C"}
print(dictTest2)
print(dictTest2[2])
del dictTest2[2]
print(dictTest2)
print(dictTest2.keys())
print(dictTest2.values())
print(dictTest2.items())


#list comprehension
# [expression for item in iterable]
# [expression for item in iterable if condition]
listComp = [x for x in range(10)]
print(listComp)
listComp = [x for x in range(10) if x % 2 == 0]
print(listComp)
listCompWords = [x for x in "word"]
print(listCompWords)