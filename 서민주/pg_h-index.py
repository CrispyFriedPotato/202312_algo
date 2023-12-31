'''
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42747
풀이 일자: 2023년 12월 28일
'''

def solution(citations):
    n = len(citations)
    citations.sort(reverse=True)
    
    for i in range(n):
        if citations[i]<i+1:
            return i
    return n