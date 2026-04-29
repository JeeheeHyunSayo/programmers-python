def solution(a, b, n):
    answer = 0
    while n >= a:
        new = n // a
        left = n % a
        n = new * b + left
        answer += new * b # answer += new (X), new 는 묶음의 수, 개수 * b
    return answer

# 한 번 반복될 때마다 변수가 어떻게 변하는지 관찰
# 시뮬레이션 문제
# (1) 상태가 계속 바뀐다
# (2) 규칙을 그대로 따라 가면 된다
# (3) while 종료 조건
