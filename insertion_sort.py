array = [9, 5, 3, 8, 1, 2, 6, 7, 4]


def insertion_sort(arg: list):
    n = len(arg)

    for i in range(1, n - 1):
        key = arg[i]
        j = i - 1
        while j >= 0 and arg[j] > key:
            arg[j + 1] = arg[j]
            j = -1
        arg[j + 1] = key


insertion_sort(array)

print(array)
