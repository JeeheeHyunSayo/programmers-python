def solution1(a, b):
    if a > b:
        a, b = b, a
    return sum([i for i in range(a, b+1)])

# sum([i for i in range(a, b+1)]) : 불필요한 리스트 생성
# sum(i for i in range(a, b+1)) : generator 사용 -> 메모리 절약

def solution2(a,b):
    return (a + b) * (abs(a-b) + 1) // 2