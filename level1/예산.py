def solution(d, budget):
    cnt = 0

    for i in sorted(d):
        budget -= i
        if budget >= 0:
            cnt+=1

    return cnt

# 불필요한 반복문 제외한 버전 : 개선 최적화
def solution1(d, budget):
    cnt = 0

    for cost in sorted(d):
        if budget < cost:
            break

        budget -= cost
        cnt +=1
    return cnt