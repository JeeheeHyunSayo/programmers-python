def solution(n):
    return '수박' * (n//2) if n % 2 == 0 else '수박' * (n//2) + '수'

#
def solution1(n):
    return ('수박' * (n//2)) + ('수' if n % 2 else '')