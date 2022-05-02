class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        solution = list()
        solution.append(nums[0])
        for i in range(1,len(nums)):
            solution.append(nums[i] + solution[i-1])
        
        return solution
                
