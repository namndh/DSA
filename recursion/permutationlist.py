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
        clone = num_range.copy()
        arr[i] = num_range[idx]
        del clone[idx]
        solution(num_range, n, arr, n+1)