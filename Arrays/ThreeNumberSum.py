def threeNumberSumSolution1(array, targetSum):
    triplets = []
    array.sort()
    for i in range(len(array) - 2):
        for j in range(len(array) - 1):
            for k in range(len(array)):
                if array[i] + array[j] + array[k] == targetSum:
                    triplets.append([array[i], array[j], array[k]])
    # print(sorted(triplets, key=lambda triplets: (triplets[0],triplets[1],triplets[2])))
    return triplets


def threeNumberSumSolution2(array, targetSum):
    # orderd in ascending with non repetitive combinations
    triplets = []
    array.sort()
    for index in range(len(array) - 2):
        left = index + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[index] + array[left] + array[right]
            if currentSum == targetSum:
                triplets.append([array[index], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            else:
                right -= 1
    return triplets



output1 = threeNumberSumSolution1([12, 3, 1, 2, -6, 5, -8, 6], 0)
print(output1)

output2 = threeNumberSumSolution2([12, 3, 1, 2, -6, 5, -8, 6], 0)
print(output2)

