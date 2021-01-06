def isValidSubsequenceSolution1(array, sequence):
    # Write your code here.
    if set(array) & set(sequence) == set(sequence):
        return True
    else:
        return False

def isValidSubsequenceSolution1(array, sequence):
    arrayIndex=0
    sequenceIndex=0
    while arrayIndex<len(array) and sequenceIndex<len(sequence):
        if array[arrayIndex]==sequence[sequenceIndex]:
            sequenceIndex+=1
        arrayIndex+=1
    return arrayIndex == len(sequence)


output = isValidSubsequenceSolution1([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 10])
print(output)

output1 = isValidSubsequenceSolution1([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 10])
print(output1)