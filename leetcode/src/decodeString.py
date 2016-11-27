def decodeString(s):
    numStack = []
    strStack = [""]
    i, n = 0, len(s)
    if n == 0:
        return ""
    while i < n:
        if s[i].isdigit():
            start = i
            while i < n and s[i].isdigit():
                i += 1
            numStack.append(int(s[start : i]))
            i -= 1
        elif s[i] == '[':
            strStack.append("")
        elif s[i] == ']':
            temp = strStack.pop()
            temp = numStack.pop() * temp
            strStack.append(strStack.pop() + temp)
        else:
            strStack.append(strStack.pop() + s[i])
        i += 1
    return strStack.pop()


print decodeString("3[a]2[bc]")
print decodeString("3[a2[c]]")
print decodeString("2[abc]3[cd]ef")

