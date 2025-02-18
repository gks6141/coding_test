def solution(s):
    stack = []
    answer = True
    
    for i in s:
        if i == "(" :
            stack.append(i)
        else:
            if stack == []:
                answer = False
            else:
                stack.pop()      
    
    if stack != [] :
        answer = False
    
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print(answer)

    return answer