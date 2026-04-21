def solution(seoul):
    for i in range(len(seoul)):
        if 'Kim' == seoul[i]:
            return f'김서방은 {i}에 있다'

# index 사용
def solution1(seoul):
    idx = seoul.index('Kim')
    return f'김서방은 {idx}에 있다'