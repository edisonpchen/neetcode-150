# 1: https://leetcode.com/problems/contains-duplicate/submissions/
def containsDuplicate(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] != 1:
            return True
    return False


assert containsDuplicate([1, 2, 3, 1]) is True
