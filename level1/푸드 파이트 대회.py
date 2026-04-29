def solution(food):
    part = ''
    answer = ''
    for i in range(1, len(food)):
        part += str(i) * (food[i] // 2)
    answer = part + '0' + part[::-1]
    return answer

# 문자열은 immutable 이기 때문에 문자열을 += 하는 것보다, 리스트 + join 을 쓰는 것이 효과적
def solution1(food):
    left_parts = []
    for i in range(1, len(food)):
        left_parts.append(str(i) * (food[i] // 2))
    left = ''.join(left_parts)
    return left + '0' + left[::-1]