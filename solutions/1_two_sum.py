class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = [e for e in nums]
        nums_sorted.sort()
        
        i = 0
        j = len(nums_sorted) - 1
        while i < j:
            two_sum = nums_sorted[i] + nums_sorted[j]
            if two_sum == target:
                index_i = nums.index(nums_sorted[i])
                if nums_sorted[i] == nums_sorted[j]:
                    return list([index_i, nums.index(nums_sorted[j], index_i + 1)])
                else:
                    return list([index_i, nums.index(nums_sorted[j])])
            elif two_sum < target:
                i += 1
                while i > j and (nums_sorted[i] == nums_sorted[i-1]):
                    i += 1
            else:
                j -= 1
                while i > j and (nums_sorted[i] == nums_sorted[i+1]):
                    j -= 1
