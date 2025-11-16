n = int(input().strip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(n-1):
    if A[i] != B[i]:
        cnt += 1
        A[i] ^= 1
        A[i+1] ^= 1
print("Output:")
print(cnt if A == B else -1)