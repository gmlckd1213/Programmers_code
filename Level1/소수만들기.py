def solution(nums):
    for i in range(len(nums)):
         for j in range(len(nums)):
             for k in range(len(nums)):
                if i==j or j==k or i == j == k:
                     continue
                else:
                    answer = nums[i]+nums[j]+nums[k]
                    if sosu(answer) == True:
                        cnt += 1
    return cnt 

def sosu(n):
    if n== 0 or n == 1:
        return False
    else:
        for i in range(2,n//2+1):
            if n%i == 0:
                return False
        return True

                