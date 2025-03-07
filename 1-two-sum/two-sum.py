class Solution(object):
    def twoSum(self, nums, target):

        for pointer in range(0,len(nums)):
            for i in range(pointer+1,len(nums)):
                if pointer != i and nums[i]+nums[pointer] == target:
                    return(pointer,i)
        