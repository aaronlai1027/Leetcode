class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return None
        cand1,cand2,count1,count2 = None, None, 0, 0
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        if nums.count(cand1) > len(nums)/3 and nums.count(cand2) > len(nums)/3:
            return [cand1,cand2]
        elif nums.count(cand1) > len(nums)/3:
            return [cand1]
        elif nums.count(cand2) > len(nums)/3:
            return [cand2]
        else: return None
