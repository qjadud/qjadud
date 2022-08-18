N = int(input())

dp = [0] * (N+1) #dp[1]은 1번쩨

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    ##계산한 횟수 저장
print(dp[N])
