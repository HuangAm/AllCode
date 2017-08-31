"""
Example:
    Given nums = [2,7,11,15], target = 9,
    Because nums[0] + nums[1] = 2+7 =9
    return [0,1]
"""
#方法一：
def two_sum(li,target):
    l = len(li)
    for i in range(l):
        for j in range(i+1,l):
            # print(li[i],li[j])
            if li[i] + li[j] == target:
                return (i,j)
    return None

#方法二：
def bin_search(li,val):


def two_sum2(li,target):
    for i in range(len(li)):
        b = target - li[i]
        j = bin_search(li,b)
        return i,j



nums = [2,7,11,15]
print(two_sum(nums,9))
