def solution1(n):
    for i in range(1, n):
        if n % i == 1:
            return i

# 최적화
def solution2(n):
    # 나머지가 1이 되는 수 찾기 -> n-1 의 약수 찾기!
    for i in range(2, int((n-1)**0.5) + 1):
        if (n-1) % i == 0:
            return i
    return n-1