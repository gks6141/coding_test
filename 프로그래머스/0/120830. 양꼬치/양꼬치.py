def solution(n, k):
    coke = 2000 * (k - n // 10) 
    answer = n * 12000 + coke 
    return answer