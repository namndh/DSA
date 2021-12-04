t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    stack = []
    res = ''
    for i in range(0, n):
        while len(stack) > 0 and stack[-1][0] >= a[i]:
            stack.pop()
        stack.append((a[i], i))
        if i >= k - 1:
            if stack[0][1] < i - k + 1:
                stack.pop(0)
            res += str(stack[0][0]) + " "
    print(res[:-1])
    
