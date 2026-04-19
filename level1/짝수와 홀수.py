def solution1(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

# 더 간략하게
def solution(num):
    return 'Even' if num % 2 == 0 else 'Odd'