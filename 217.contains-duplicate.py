class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in nums:
            if i in hash:
                return True
            hash[i] = True
        return False
