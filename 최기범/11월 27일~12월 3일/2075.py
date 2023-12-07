# 우선 순위 큐 사용 (삽입된 원소를 자동으로 정렬해준다)
import heapq
n = int(input())
heap = []
for _ in range(n) :
    arr = list(map(int,input().split()))
    for i in arr :
        # 만약 우선순위 큐 개수가 n보다 적다면 무조건 삽입
        if len(heap) < n :
            heapq.heappush(heap,i)
        else :
        # 우선순위 큐 첫번째 원소보다 입력된 원소가 크다면
            if heap[0] < i :
            # 첫번째 원소 제거 
                heapq.heappop(heap)
            # 입력된 원소 삽입
                heapq.heappush(heap,i)
#첫번째 원소 출력
print(heap[0])

