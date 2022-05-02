class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high - low + 1) // 2 if (high - low + 1) % 2 == 0 else ((high - low + 1) // 2 + 1 if (low % 2 != 0) or (high % 2 != 0) else (high - low + 1) // 2)

            
            
    # (high - low + 1) -> Total of numbers between low and high, both included
    # (high - low + 1) // 2 -> Total of odd if Total numbers is even
    # (high - low + 1) // 2 -> Total of even if Total numbers is even
    # (high - low + 1) // 2 + 1 -> Total of odd if Total numbers is not even and one of
        # both low or high is odd
    # Total of numbers - (high - low + 1) // 2 + 1 -> Total of even if Total numbers is not even and one of
        # both low or high is odd
    # (high - low + 1) // 2 -> Total of odd if Total of numbers is not even and both low and high are even
    # Total of numbers - (high - low + 1) // 2 -> Total of even if Total of numbers is not even and 
        # both low and high are even
