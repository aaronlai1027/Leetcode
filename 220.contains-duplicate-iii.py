class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k <= 0 or t < 0: return False
        key_to_val = {}
        for i, num in enumerate(nums):
            key = num // (t + 1)
            if key in key_to_val \
                    or key + 1 in key_to_val and key_to_val[key + 1] - num <= t \
                    or key - 1 in key_to_val and num - key_to_val[key - 1] <= t:
                return True
            if i >=k:
                del key_to_val[nums[i-k] // (t + 1)]
            key_to_val[key] = num
        return False
