def solution(n, m):
    answer = []
    if n >= m:
        n, m = m, n
        # 최대 공약수 (m,n의 약수인지 체크를 안해서 틀림;)
    for i in range(n, 0, -1):
        if m % i == 0 and n % i == 0:
            answer.append(i)
            break
            # 최소 공배수
    answer.append(n*m//answer[0])
    return answer

def solution1(n, m):
    def gcb(a,b):
        while b:
            a,b = b, a%b
        return a

    g = gcb(n,m)
    return [g, n*m//g]