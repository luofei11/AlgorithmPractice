def getMaxUtil(nums, length):
    stack = []
    for i in range(len(nums)):
        if not stack:
            stack.append(nums[i])
        else:
            while stack[-1] < nums[i] and len(stack) - 1 + len(nums) - i >= length:
                stack.pop()
            stack.append(nums[i])
    return ''.join([str(x) for x in stack[:length]])


print getMaxUtil([9,1,2,2,8,3], 4)
print getMaxUtil([9,1,2,5,8,3], 6)
