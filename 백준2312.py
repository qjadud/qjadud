testcase = int(input())  #테스트 케이스 수 입력
for i in range(testcase):
    N = int(input())   #소인수분해할 수를 입력받음
    for i in range(2, N+1):
        cnt = 0
        if N % i == 0:
            while N % i == 0:
                N //= i
                cnt += 1
                ##cnt를 증가 시키면서 N에 나눈 몫을 넣어줌
            print(i, cnt)
        elif N == 1:
            break
        ##N이 1이 되면 for문 탈출
