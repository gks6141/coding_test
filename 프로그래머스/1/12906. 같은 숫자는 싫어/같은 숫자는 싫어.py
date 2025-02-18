def solution(arr):
    stack = []
    answer = []
        
    for i in arr:
            if len(answer) == 0 or i != answer[-1]:
                answer.append(i)
            else :
                pass
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    return answer