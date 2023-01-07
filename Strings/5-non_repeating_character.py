
def nonrepeatingCharacter(s):
    repeats = {}
    for i in range(len(s)):
        if s[i] not in repeats:
            repeats[s[i]] = 1
        else:
            repeats[s[i]] += 1
    for i in range(len(s)):
        if repeats[s[i]] == 1:
            return s[i]
    return '$'
# Time Complexity-O(N)
# Space Complexity-O(N)
