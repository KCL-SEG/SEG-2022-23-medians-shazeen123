


while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)


list = [1, 3, 5, 2]
list.sort()

if list.__len__() % 2 == 0:
    median = (list[list.__len__() / 2] + list[(list.__len__() - 2) / 2]) / 2
else:
    median = list[(list.__len__() - 1) / 2]

print(median)
//