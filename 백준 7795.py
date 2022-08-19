from bisect import bisect_left, bisect_right

T = int(input()) #테스트 케이스의 개수
for _ in range(T):
    _, _ = map(int, input().split()) #A의 수 N과 B의 수 M
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    B.sort() #bisect_left()를 사용하기 위해 오름차순 정렬
    
    num = 0  #출력 값 초기화
    for i in A:
        num += bisect_left(B, i)
        #B의 원소 중에 A의 원소 보다 작은 개수 누적합
    print(num)
