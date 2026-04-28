from itertools import combinations
def solution(numbers):
    answer = set()
    for i in combinations(numbers, 2):
        answer.add(sum(i))
    return sorted(answer)

def solution1(numbers):
    return sorted({a + b for a, b in combinations(numbers, 2)})