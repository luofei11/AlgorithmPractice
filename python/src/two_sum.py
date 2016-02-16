# find if there are 2 elements in the array that have a sum of target
# @return a tuple, (index1, index2)
def twoSum(num,target):
    map = dict()
    for i in range(len(num)):
        map[num[i]] = i
    for i in range(len(num)):
        if (target - num[i]) in map and map[target - num[i]] != i:
            return i + 1, map[target - num[i]] + 1
