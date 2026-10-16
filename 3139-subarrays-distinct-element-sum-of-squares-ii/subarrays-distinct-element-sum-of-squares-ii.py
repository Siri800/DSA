class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        tree = [0] * (4 * n)
        lazy = [0] * (4 * n)
        def update(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                tree[node] += val * val * (end - start + 1)
                lazy[node] += val
                return

            mid = (start + end) // 2
            left = node * 2
            right = left + 1

            if lazy[node]:
                v = lazy[node]
                length1 = mid - start + 1
                length2 = end - mid

                tree[left] += 2 * v * tree[left] * 0 + v * v * length1
                tree[right] += 2 * v * tree[right] * 0 + v * v * length2
                lazy[left] += v
                lazy[right] += v
                lazy[node] = 0

            update(left, start, mid, l, r, val)
            update(right, mid + 1, end, l, r, val)

        # Segment tree storing sum and sum of squares
        sums = [0] * (4 * n)

        def add(node, start, end, l, r, val):
            if l > end or r < start:
                return
            if l <= start and end <= r:
                tree[node] += 2 * val * sums[node] + val * val * (end - start + 1)
                sums[node] += val * (end - start + 1)
                lazy[node] += val
                return

            mid = (start + end) // 2
            left = node * 2
            right = left + 1

            if lazy[node]:
                v = lazy[node]
                for child, length in ((left, mid - start + 1),
                                      (right, end - mid)):
                    tree[child] += 2 * v * sums[child] + v * v * length
                    sums[child] += v * length
                    lazy[child] += v
                lazy[node] = 0

            add(left, start, mid, l, r, val)
            add(right, mid + 1, end, l, r, val)
            sums[node] = sums[left] + sums[right]
            tree[node] = tree[left] + tree[right]

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            p = last.get(x, -1)
            add(1, 0, n - 1, p + 1, i, 1)
            ans = (ans + tree[1]) % MOD
            last[x] = i

        return ans