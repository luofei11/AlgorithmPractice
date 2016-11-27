def leftSumEqualRightSum(array):
    total = sum(array)
    currSum = 0
    for num in array:
        if total - currSum - num == currSum:
            return True
        currSum += num
    return False


print leftSumEqualRightSum([1,2,3,5,3,2,1])
