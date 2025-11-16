n = int(input().strip())
sA = input().strip()
sB = input().strip()

def parse(line, n):
    if ' ' in line:
        arr = list(map(int, line.split()))
    else:
        arr = [int(ch) for ch in line if ch in '01']
    if len(arr) != n:
        print("Format input salah")
        exit()
    return arr

A = parse(sA, n)
B = parse(sB, n)

c = 0
for i in range(n-1):
    if A[i] != B[i]:
        c += 1
        A[i] ^= 1
        A[i+1] ^= 1

print("Output:")
print(c if A == B else -1)



