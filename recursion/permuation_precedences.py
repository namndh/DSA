def display(permutation):
    for i in range(len(permutation)):
        if i < len(permutation) - 1:
            print(permutation[i], end=" ")
        else:
            print(permutation[i])


def solution(num_range, n, arr, i, permutations):
    if i == n:
        permutations.append("".join(list(map(str, arr))))
        return

    if len(num_range) == 0:
        return

    for idx in range(len(num_range)):
        clone = num_range.copy()
        arr[i] = num_range[idx]
        del clone[idx]
        solution(clone, n, arr, i + 1, permutations)


n = int(input())
k = int(input())
precedences = []
for i in range(k):
    next_line = input()
    precedences.append(next_line.split(" "))

num_range = list(range(1, n + 1))
permutations = []
arr = [None] * n
solution(num_range, n, arr, 0, permutations)

result_count = 0
result = []
for permu in permutations:
    wrong_precedences = 0
    for p in precedences:
        for i in range(len(p) - 1):
            if permu.index(p[i]) > permu.index(p[i + 1]):
                wrong_precedences += 1
    if wrong_precedences == 0:
        display(permu)
        result_count += 1
print(result_count)
