smallest = None
largest = None

for value in ([5, 6, 7, 19, 58, 72, 1, 3, 56, 41, 89, 56, 15, 23, 32, 0]):
    if largest is None:
        largest = value
    elif value > largest:
        largest = value
    elif smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
print(smallest, largest,)
