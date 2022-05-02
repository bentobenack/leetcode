class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        solution = list()
        x = 0
        y = n
        
        while x < n:
            solution.append(nums[x])
            solution.append(nums[y])
            
            x += 1
            y += 1
            
        return solution
