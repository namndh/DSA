raw_input = input()
while raw_input != '0':
    inp = list(map(int, raw_input.split(" ")))
    n = inp[0]
    recs = [-1]
    recs.extend(inp[1:])
    l = [-1 for _ in range(n+1)]
    r = [-1 for _ in range(n+1)]
    stack_left, stack_right = [(-1, 0)], [(-1, n+1)]
    for i in range(1, n+1):
        while stack_left[-1][0] >= recs[i]:
            stack_left.pop()
        l[i] = stack_left[-1][1] + 1
        stack_left.append((recs[i], i))

    for i in range(n, 0, -1):
        while stack_right[-1][0] >= recs[i]:
            stack_right.pop()
        r[i] = stack_right[-1][1] - 1
        stack_right.append((recs[i], i))
    res = 0
    for i in range(n+1):
        res = max(res, recs[i]*(r[i] - l[i] + 1))
    print(res)
    raw_input = input()
