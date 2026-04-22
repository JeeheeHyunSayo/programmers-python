def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            arr1[i][j] += arr2[i][j]
    return arr1

def solution1(arr1, arr2):
    return [[a+b for a, b in zip(r1, r2)] for r1, r2 in zip(arr1, arr2)]