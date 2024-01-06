def solve():
    N = int(input())
    array = []

    for _ in range(N):
        array.append(int(input()))

    # перевернем массив
    reversed_array = array[::-1]

    # выведем перевернутый массив
    for num in reversed_array:
        print(num)

solve()