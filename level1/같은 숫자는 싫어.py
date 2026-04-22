def solution(arr):
    answer = [arr[0]] # 첫 번째 항부터 비교
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]: # 이전 값 != 현재값 -> 넣기
            answer.append(arr[i])
    return answer