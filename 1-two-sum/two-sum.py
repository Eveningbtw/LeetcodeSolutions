class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        Map = {} #Value, Index

        for index, number in enumerate(nums):
            difference = target - number
            if difference in Map:
                return [Map[difference], index]
            Map[number] = index
        return 0 # Incase Failure
