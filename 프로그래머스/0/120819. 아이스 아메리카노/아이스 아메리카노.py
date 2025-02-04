def solution(money):
    glass = money // 5500
    result = money - (glass * 5500)
    
    answer = [glass, result]
    return answer