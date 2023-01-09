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

