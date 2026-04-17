def solution(n):
    value = n ** 0.5
    if value.is_integer():
        return (value +1) ** 2
    else:
        return -1