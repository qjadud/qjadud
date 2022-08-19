'''
사용한 알고리즘
1. a[k] < a[k+1]가 성립하는 k의 최댓값을 찾는다.(만약 k값이 존재하지 않으면 내림차순으로 정렬 되어 있음)
2. 인덱스 k 이후의 값들 중 a[k] < a[m]이 성립하는 m의 최댓값을 찾는다.
3. k와 m 자리의 값을 서로 바꾸어 준다.
4. 인덱스 k 이후의 값들을 오름차순으로 정렬해준다.
'''
N = int(input())
s = list(map(int, input().split())) #순열 입력

k = 0  #초기화
## 알고리즘 1.k의 최댓값 구하기
for i in range(len(s)-1):
    if s[i] < s[i+1]:
        k = i
        
if k == 0: #내립차순인 경우
    print(-1)
else:
    ## 알고리즘 2.m의 최댓값 구하기
    for i in range(k+1, len(s)):
        if s[k] < s[i]:
            m = i
    ## 알고리즘 3. k와 m의 값 바꾸기
    s[k], s[m] = s[m], s[k]
    ## 알고리즘 4.오름차순 정렬
    t = s[k+1 : ]
    t.sort()
    n = s[ : k+1] + t
    
    for num in n:
        print(num, end=' ')
