class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        arr = sorted((value, index) for index, value in enumerate(nums))
        groups = []
        current = []
        for i in range(n):
            if i == 0 or arr[i][0] - arr[i - 1][0] <= limit:
                current.append(arr[i])
            else:
                groups.append(current)
                current = [arr[i]]
        groups.append(current)
        ans = nums[:]
        for group in groups:
            values = sorted(value for value, _ in group)
            indices = sorted(index for _, index in group)
            for idx, value in zip(indices, values):
                ans[idx] = value
        return ans