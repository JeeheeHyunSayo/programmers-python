def solution1(s):
    # 단 개수를 비교할 때 대문자와 소문자는 구별하지 않음
    s = s.lower()
    cnt_p = s.count('p')
    cnt_y = s.count('y')
    if cnt_p == 0 and cnt_y == 0:
        return True
    if cnt_p == cnt_y:
        return True
    else:
        return False

# 더 효율적으로, 불필요한 비교 줄이기
def solution2(s):
    s = s.lower()
    return s.count('p') == s.count('y')