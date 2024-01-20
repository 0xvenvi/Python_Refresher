dataArray = []
dataArray.insert(0, "apple")
print(dataArray)
dataArray.insert(0, "orange")
print(dataArray)
dataArray.insert(1, "guava")
print(dataArray)
dataArray.remove("apple")
print(dataArray)

print(len(dataArray))

op = ["a", "b", "c", "d", "e", "f", "g", "h"]
num_op = len(op)
print(num_op)

# while x in op:
#     print(x)


# for data in op:
#     dataArray.add(data)
#     print(dataArray)


op1 = ["a", "b", "c", "d", [1, 2, 3, 4, 5], "f", "g", ["The", True, 10.10, 100]]
print(op1[4])
