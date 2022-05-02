class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = list()

        for i in range(len(nums) - 2):
            if i > 0 and (nums[i-1] == nums[i]):
                continue
            
            j,k = i + 1, len(nums) - 1

            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]

                if three_sum == 0:
                    solution.append([nums[i],nums[j], nums[k]])

                    j += 1
                    k -= 1

                    while j < k and (nums[j-1] == nums[j]):
                        j += 1
                    while j < k and (nums[k+1] == nums[k]):
                        k -= 1
                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1 

        return solution
