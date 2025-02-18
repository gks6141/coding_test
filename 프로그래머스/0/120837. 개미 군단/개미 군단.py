def solution(hp):
    
    hero = hp//5 
    nomal= (hp-(hero*5)) //3
    work = hp-(hero*5)-(nomal*3)
    
    answer = hero + nomal + work

    return answer