# 1: https://leetcode.com/problems/contains-duplicate/submissions/
def containsDuplicate(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
        if count[num] != 1:
            return True
    return False


# 2: https://leetcode.com/problems/valid-anagram/description/
def isAnagram(self, s, t):
    count_s, count_t = {}, {}
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1

    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False
    return True


# 3: https://leetcode.com/problems/two-sum/
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []


# 4: https://leetcode.com/problems/group-anagrams/
def groupAnagrams(self, strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    map = dict()
    for i in range(len(strs)):
        temp = list(strs[i])
        print(temp)
        temp.sort()
        temp2 = "".join(temp)
        if map.get(temp2) is None:
            map[temp2] = [strs[i]]
        else:
            map[temp2].insert(0, strs[i])

    return map.values()

    
# 5: https://leetcode.com/problems/valid-palindrome/
def isPalindrome(self, s: str) -> bool:
    s = "".join(c for c in s if c.isalnum()).lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
