def solution(n):
    answer = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            answer += i
            # i 가 n의 약수인 경우 pair 합 구하기
            if i != n // i:
                answer += n//i
    return answer