class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        # Count characters
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        # A palindrome can have at most one odd frequency
        if sum(x % 2 for x in freq) > 1:
            return ""

        # Middle character for odd length
        mid = ""
        for i in range(26):
            if freq[i] % 2:
                mid = chr(ord('a') + i)
                break

        # Only half of each character is needed on the left
        for i in range(26):
            freq[i] //= 2

        half = n // 2

        # Answer array
        ans = list(s)

        # Construct complete palindrome from left half
        def make_palindrome():
            if mid:
                ans[half] = mid

            for i in range(half):
                ans[n - 1 - i] = ans[i]

        # First, try to make the left half equal to target's left half
        pos = 0

        while pos < half:
            c = ord(target[pos]) - ord('a')

            if freq[c] == 0:
                break

            ans[pos] = target[pos]
            freq[c] -= 1
            pos += 1

        # If we matched the complete left half,
        # the right half is forced.
        if pos == half:
            make_palindrome()

            candidate = ''.join(ans)

            if candidate > target:
                return candidate

        # Backtrack to find the first position
        # where we can put a character greater than target[pos].
        while True:

            if pos < half:

                target_char = ord(target[pos]) - ord('a')

                # Find smallest available character
                # strictly greater than target[pos]
                for c in range(target_char + 1, 26):

                    if freq[c] > 0:

                        ans[pos] = chr(ord('a') + c)
                        freq[c] -= 1

                        # Fill remaining positions with
                        # the smallest possible characters
                        idx = pos + 1

                        for ch in range(26):
                            for _ in range(freq[ch]):
                                ans[idx] = chr(ord('a') + ch)
                                idx += 1

                        # Mirror left half
                        make_palindrome()

                        return ''.join(ans)

            # No larger character possible here.
            # Move one position backward.
            if pos == 0:
                return ""

            pos -= 1

            # Restore the character that matched target[pos]
            c = ord(target[pos]) - ord('a')
            freq[c] += 1