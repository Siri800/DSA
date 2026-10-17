class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = sorted(nums, key=lambda x: (sum(map(int, str(x))), x))
        pos = {v: i for i, v in enumerate(nums)}
        ans = 0

        for i, v in enumerate(arr):
            j = pos[v]
            if i != j:
                nums[i], nums[j] = nums[j], nums[i]
                pos[nums[j]] = j
                pos[nums[i]] = i
                ans += 1

        return ans