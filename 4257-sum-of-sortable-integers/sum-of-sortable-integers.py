class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            prev_max = float('-inf')

            for start in range(0, n, k):
                block = nums[start:start + k]

                if prev_max > min(block):
                    valid = False
                    break

                descents = 0
                for i in range(k - 1):
                    if block[i] > block[i + 1]:
                        descents += 1

                if block[-1] > block[0]:
                    descents += 1

                if descents > 1:
                    valid = False
                    break

                prev_max = max(block)

            if valid:
                ans += k

        return ans
