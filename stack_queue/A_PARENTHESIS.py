s = input()
if len(s) % 2 != 0:
    print(0)
else:
    stack = []
    res = 0
    for p in s:
        if (p == "(") or (p == "[") or (p == "{"):
            stack.append(p)
        elif p == ")" and len(stack) > 0 and stack[-1] == "(":
            stack.pop()
        elif p == "}" and len(stack) > 0 and stack[-1] == "{":
            stack.pop()
        elif p == "]" and len(stack) > 0 and stack[-1] == "[":
            stack.pop()
        else:
            res = 0
            break
    res = int(len(stack) == 0)
    print(res)