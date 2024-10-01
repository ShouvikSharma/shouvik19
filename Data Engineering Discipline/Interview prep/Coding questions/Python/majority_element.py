class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        empty_dict = {}

        for i,n in enumerate(nums):
            if n in empty_dict:
                empty_dict[n] += 1
            else: 
                empty_dict[n] = 1

            if empty_dict[n] > (len(nums)/2):
                return n



### https://leetcode.com/problems/majority-element/?envType=problem-list-v2&envId=array