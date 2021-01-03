import itertools


def twoNumberSum(array, targetSum):
    flag = False
    if len(array) < 1 or len(array) == 1:
        return []
    else:
        for count, numbers in enumerate(itertools.combinations(array, 2)):
            if sum(numbers) == targetSum:
                flag = True
                return [number for number in numbers]
            # print([array.index(number) for number in numbers])( to print index)
        if not flag:
            return []


output = twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164)
print(output)


def twoNumberSumSolution2(array, targetSum):
    for index in range(len(array) - 1):
        firstNum = array[index]
        for nextIndex in range(len(array) - 1):
            secondNum = array[nextIndex]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []


# O(n^2) time| O(1) space

output = twoNumberSumSolution2([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164)
print(output)


def twoNumberSumSolution3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1
    return []


# O(n log n) time| O(1) space

output = twoNumberSumSolution3([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164)
print(output)


def twoNumberSumSolution4(array, targetSum):
    pass
