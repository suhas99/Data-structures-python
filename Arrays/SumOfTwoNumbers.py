import itertools


def twoNumberSum(array, targetSum):
    # Write your code here.
    if len(array) < 1 or len(array) == 1:
        return []
    else:
        product=itertools.combinations(array, 2)
        for count,numbers in enumerate(product):
            print(count)
            if sum(numbers) == targetSum:
                return [number for number in numbers]
                # print([number for number in numbers])
                # print([array.index(number) for number in numbers])


output=twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164)
print(output)
