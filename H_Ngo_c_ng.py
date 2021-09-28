if len(s) % 2 != 0:
    return False
stack = []
le
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
        print(0)
    
return len(stack) == 0