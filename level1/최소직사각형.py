def solution(sizes):
    max_w = 0
    max_h = 0
    for size in sizes:
        # sizes = [[w, h], [w,h], .., ] w 에 최대값, h 에 최소값
        w, h = max(size), min(size)
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    return max_w * max_h