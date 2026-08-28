class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        if sum(x % 2 for x in freq) > 1:
            return ""
        mid = ""
        for i in range(26):
            if freq[i] % 2:
                mid = chr(ord('a') + i)
                break
        for i in range(26):
            freq[i] //= 2
        half = n // 2
        ans = list(s)
        def make_palindrome():
            if mid:
                ans[half] = mid
            for i in range(half):
                ans[n - 1 - i] = ans[i]
        pos = 0
        while pos < half:
            c = ord(target[pos]) - ord('a')
            if freq[c] == 0:
                break
            ans[pos] = target[pos]
            freq[c] -= 1
            pos += 1
        if pos == half:
            make_palindrome()
            candidate = ''.join(ans)
            if candidate > target:
                return candidate
        while True:
            if pos < half:
                target_char = ord(target[pos]) - ord('a')
                for c in range(target_char + 1, 26):
                    if freq[c] > 0:
                        ans[pos] = chr(ord('a') + c)
                        freq[c] -= 1
                        idx = pos + 1
                        for ch in range(26):
                            for _ in range(freq[ch]):
                                ans[idx] = chr(ord('a') + ch)
                                idx += 1
                        make_palindrome()
                        return ''.join(ans)
            if pos == 0:
                return ""
            pos -= 1
            c = ord(target[pos]) - ord('a')
            freq[c] += 1