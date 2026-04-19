def solution1(x):
    answer = True
    total = 0
    for i in str(x):
        total += int(i)
    # 부분 합을 다 구한 뒤
    if x % total != 0:
        answer = False
    return answer

def solution2(x):
    total = sum(int(i) for i in str(x))
    return x % total == 0