

def min_arr(arr):
    min = arr[0]

    for el in arr:
        if min > el:
            min = el

    return min


def avg_arr(arr):
    sum = 0

    for el in arr:
        sum += el

    return sum / len(arr)


arr = [1, 2, 3, 4, 5]
arr1 = [6, 7, 8, 9, 10]

print(min_arr(arr))
print(min_arr(arr1))
print(avg_arr(arr))
print(avg_arr(arr1))
