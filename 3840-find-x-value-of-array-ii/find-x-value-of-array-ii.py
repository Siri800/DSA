class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        tree = [[1, [0] * k] for _ in range(4 * n)]
        def merge(a, b):
            p1, c1 = a
            p2, c2 = b
            p = (p1 * p2) % k
            c = c1[:]
            for r in range(k):
                c[(p1 * r) % k] += c2[r]
            return [p, c]
        def build(node, l, r):
            if l == r:
                rem = nums[l] % k
                tree[node] = [rem, [0] * k]
                tree[node][1][rem] = 1
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
        def update(node, l, r, idx, val):
            if l == r:
                rem = val % k
                tree[node] = [rem, [0] * k]
                tree[node][1][rem] = 1
                return
            mid = (l + r) // 2
            if idx <= mid:
                update(node * 2, l, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, r, idx, val)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
        def query(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                return tree[node]
            mid = (l + r) // 2
            if qr <= mid:
                return query(node * 2, l, mid, ql, qr)
            if ql > mid:
                return query(node * 2 + 1, mid + 1, r, ql, qr)
            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)
            return merge(left, right)
        build(1, 0, n - 1)
        ans = []
        for index, value, start, x in queries:
            nums[index] = value
            update(1, 0, n - 1, index, value)
            res = query(1, 0, n - 1, start, n - 1)
            ans.append(res[1][x])
        return ans