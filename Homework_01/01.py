K = int(input())
NumsStr = input().split()
Nums = list(map(int, NumsStr)) # map

# algorithm 4. O(N)

# algorithm 3. O(NlogN)

# algorithm 2. O(N**2)
MaxSum = 0
for i in range(K):
    ThisSum = 0
    for j in range(K)[i:]:
        ThisSum += Nums[j]
        if ThisSum > MaxSum:
            MaxSum = ThisSum
print(MaxSum)

# algorithm 1. O(N**3)
MaxSum = 0
for i in range(K):
    for j in range(K)[i:]:
        ThisSum = 0
        for k in range(i, j+1):
            ThisSum += Nums[k]
        if ThisSum > MaxSum:
            MaxSum = ThisSum
print(MaxSum)
