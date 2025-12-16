from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n + 1)
        for i in range(1, n + 1):
            bits[i] = bits[i // 2] + (i & 1)
        return bits

# Example run
if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(5))  # Expected: [0,1,1,2,1,2]
