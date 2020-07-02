class Solution:
    def moveZeroes(self, nums: 'List[int]') -> 'None':
        if(len(nums)==0):
            return []
        else:
            zeroCounter=0
            for i in range(len(nums)-1,-1,-1):
                if(nums[i]==0):
                    zeroCounter+=1
                    del nums[i]
            nums.extend([0]*zeroCounter)
