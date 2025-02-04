def solution(numer1, denom1, numer2, denom2):
    numer = numer1*denom2 + numer2*denom1
    denom = denom1*denom2
    
    for i in range (numer,0,-1):
        if numer % i == 0 and denom % i == 0:
            break
            
    numer = numer/i
    denom = denom/i
    
    answer = [numer, denom]
    return answer