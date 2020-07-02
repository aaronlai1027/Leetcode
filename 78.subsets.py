class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums,res,[],0)
        return res

    def dfs(self,nums,res,tmp_list,start):
        res.append(tmp_list)
        for i in range(start,len(nums)):
            self.dfs(nums,res,tmp_list+[nums[i]],i+1)
