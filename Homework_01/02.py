K = int(input())
NumsStr = input().split()
Nums = list(map(int, NumsStr))  # map

# algorithm 4. O(N)
MaxSum = 0
ThisSum = 0
FirstIndex = 0
ZeroExist = 0
FirstNum = Nums[0]
LastNum = Nums[K-1]
for i in range(K):
    ThisSum += Nums[i]
    if ThisSum > MaxSum:
        MaxSum = ThisSum
        FirstNum = Nums[FirstIndex]
        LastNum = Nums[i]
    elif ThisSum < 0:
        ThisSum = 0
        FirstIndex = i+1
    elif Nums[i] == 0:
        ZeroExist = 1
if ZeroExist == 1 and FirstNum == Nums[0] and LastNum == Nums[K-1]:
    if FirstNum <= 0 or LastNum <= 0:
        FirstNum = 0
        LastNum = 0
print(MaxSum, FirstNum, LastNum, sep=' ')
