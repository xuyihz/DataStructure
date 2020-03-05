K = int(input())
NumsStr = input().split()
Nums = list(map(int, NumsStr))  # map

# algorithm 4. O(N)
MaxSum = 0
ThisSum = 0
for i in range(K):
    ThisSum += Nums[i]
    if ThisSum > MaxSum:
        MaxSum = ThisSum
    elif ThisSum < 0:
        ThisSum = 0
print(MaxSum)

# algorithm 3. O(NlogN)
def MaxBorderSum(List, Start, End, Step):
    MaxSum = 0
    ThisSum = 0
    for i in range(Start, End+Step, Step):
        ThisSum += List[i]
        if ThisSum > MaxSum:
            MaxSum = ThisSum
    return MaxSum

def DivideAndConquer(List, Left, Right):
    if Left == Right:  # end of recursion
        return max(List[Left], 0)

    Center = (Left + Right) // 2  # floored quotient
    MaxLeftSum = DivideAndConquer(List, Left, Center)
    MaxRightSum = DivideAndConquer(List, Center+1, Right)

    MaxLeftBorderSum = MaxBorderSum(List, Center, Left, -1)
    MaxRightBorderSum = MaxBorderSum(List, Center+1, Right, 1)
    
    return max(MaxLeftSum, MaxRightSum, MaxLeftBorderSum + MaxRightBorderSum)

MaxSum = DivideAndConquer(Nums, 0, K-1)
print(MaxSum)

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
