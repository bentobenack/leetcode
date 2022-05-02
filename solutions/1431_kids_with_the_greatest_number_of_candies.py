class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candies_sort = [e for e in candies]
        candies_sort.sort()
        max_e = candies_sort[len(candies) - 1]
        
        solution = list()
        
        for e in candies:
            if e + extraCandies >= max_e:
                solution.append(True)
            else:
                solution.append(False)
                
        return solution
