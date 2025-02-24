def solution(M, N):
    if M < N:
        answer = (M-1) + M*(N-1)
    else:
        answer = (N-1) + N*(M-1)
    return answer   