from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        a, b = nums[-1], nums[-2]
        return (a - 1) * (b - 1)

# Example run
if __name__ == "__main__":
    so = Solution()
    print(so.maxProduct([3, 4, 5, 2]))
