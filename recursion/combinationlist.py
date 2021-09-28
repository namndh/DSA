def print_arr(arr):
    for i in range(len(arr)):
        if i < len(arr) - 1:
            print(arr[i], end=" ")
        else:
            print(arr[i])


def solution(num_range, n, arr, i):
    if i == n:
        print_arr(arr)
        return

    if len(num_range) == 0:
        return

    for idx in range(len(num_range)):
        clone = num_range[idx + 1:]
        arr[i] = num_range[idx]
        solution(clone, n, arr, i + 1)


input_str = input()
m, n = list(map(int, input_str.split(" ")))
num_range = list(range(1, m + 1))
arr = [None] * n
solution(num_range, n, arr, 0)
