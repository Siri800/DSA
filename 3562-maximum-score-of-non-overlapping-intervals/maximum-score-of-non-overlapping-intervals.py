from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        arr = sorted(
            [(s, e, w, i) for i, (s, e, w) in enumerate(intervals)],
            key=lambda x: (x[1], x[0], x[3])
        )

        ends = [x[1] for x in arr]

        prev = [0] * n
        for i in range(n):
            # Previous interval must have end < current start
            prev[i] = bisect_left(ends, arr[i][0])

        dp = [[None] * 5 for _ in range(n + 1)]

        for k in range(5):
            dp[0][k] = (0, [])

        for i in range(1, n + 1):
            s, e, w, idx = arr[i - 1]

            for k in range(5):
                # Skip current interval
                best = dp[i - 1][k]

                if k > 0:
                    old_score, old_indices = dp[prev[i - 1]][k - 1]
                    candidate = (
                        old_score + w,
                        old_indices + [idx]
                    )

                    if candidate[0] > best[0]:
                        best = candidate
                    elif candidate[0] == best[0]:
                        if sorted(candidate[1]) < sorted(best[1]):
                            best = candidate

                dp[i][k] = best

        return sorted(dp[n][4][1])