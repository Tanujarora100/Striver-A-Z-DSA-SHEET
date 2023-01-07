class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        start = 0
        s = list(s)
        end = len(s)-1
        while start <= end:
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start = start+1
                end = end-1
            # Both are vowels so swap them
            elif s[start] in vowels:
                end = end-1
            # One is a vowel so stay there and find another one
            elif s[end] in vowels:
                start = start+1
            else:
                # Both are not vowels so just move forward
                start = start+1
                end = end-1
        return "".join(s)
