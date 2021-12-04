n = int(input())
s = list(map(int, input().split(" ")))

s_forward, s_backward = [], []

ans = -1

for i in range(n):
    while len(s_forward) > 0 and s[i] > s[s_forward[-1]]:
        s_forward.pop()
    if len(s_forward) > 0:
        ans = max(ans, s[i] ^ s[s_forward[-1]])
    s_forward.append(i)
    while len(s_backward) > 0 and s[n-i-1] > s[s_backward[-1]]:
        s_backward.pop()
    if len(s_backward) > 0:
        ans = max(ans, s[n-i-1] ^ s[s_backward[-1]])
    s_backward.append(n-i-1)

print(ans)
