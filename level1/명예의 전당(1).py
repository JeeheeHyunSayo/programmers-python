# 우선순위 큐
import heapq

def solution(k, score):
    heap = []
    result = []

    for s in score:
        heapq.heappush(heap, s)

        if len(heap) > k:
            heapq.heappop(heap) # 가장 작은 값 제거
        result.append(heap[0]) # 현재 명예의 전당 최솟값
    return result