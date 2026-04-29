def solution(array, commands):
    answer = []
    for p in range(len(commands)):
        i, j, k = commands[p][0], commands[p][1], commands[p][2]
        arr = sorted(array[i-1:j])
        answer.append(arr[k-1])
    return answer

# 효과적인 언팩킹
def solution1(array, commands):
    answer = []

    for i, j, k in commands:
        sub_array = sorted(array[i-1: j])
        answer.append(sub_array[k-1])

    return answer