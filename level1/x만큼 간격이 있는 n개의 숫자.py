# 원래
def solution1(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x*i)
    return answer

# 개선 : 리스트 컴프리헨션을 활용하자
def solution2(x, n):
    return [x * i for i in range(1, n+1)]

