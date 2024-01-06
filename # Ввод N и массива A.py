def rearrange_array(array):
    length = len(array)
    middle = length // 2

    if length % 2 == 0:
        result = array[:middle][::-1] + array[middle:]
    else:
        result = array[:middle + 1][::-1] + array[middle + 1:]

    return result
N = int(input())
array = list(map(int, input().split()))

new_array = rearrange_array(array)

print(*new_array)