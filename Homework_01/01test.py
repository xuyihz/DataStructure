K = int(input())
NumsStr = input().split()
Nums = list(map(int, NumsStr))  # map

# algorithm 3. O(NlogN)
def MaxBorderSum(List, Start, End, Step):
    MaxSum = 0
    ThisSum = 0
    for i in range(Start, End, Step):
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
