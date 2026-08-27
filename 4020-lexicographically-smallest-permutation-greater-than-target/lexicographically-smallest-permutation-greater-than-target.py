class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for i in range(n - 1, -1, -1):
            cnt = freq[:]
            possible = True
            for j in range(i):
                x = ord(target[j]) - ord('a')
                if cnt[x] == 0:
                    possible = False
                    break
                cnt[x] -= 1
            if not possible:
                continue
            t = ord(target[i]) - ord('a')
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1
                    ans = target[:i]
                    ans += chr(c + ord('a'))
                    for x in range(26):
                        ans += chr(x + ord('a')) * cnt[x]
                    return ans
        return ""