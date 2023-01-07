def reverseWords(S):
    res = S.split(".")
    res.reverse()
    return ".".join(res)
    # Time Complexity-O(N)
    # Space Complexity-O(1)


def reverse_stringStack(S: str) -> str:
    # Split the string by the dots
    words = S.split(".")
    stack = []
    for i in words:
        stack.append(i)
    result = ""
    # Iterate until the stack is empty
    while stack:
        # Pop a word from the stack and add it to the result string
        result += stack.pop(len(stack)-1) + "."
    # Remove the last dot from the result string
    # To remove the last do we are doing this
    # Or we can just return the array.
    return result[:-1]
# Time complexity: O(n)
# Space complexity: O(N)


# Best Approach without any data structure
def reverse_string(S: str) -> str:
    # Split the string by the dots
    words = S.split(".")
    result = ""
    # Iterate over the words in reverse order
    for i in range(len(words)-1, -1, -1):
        result += words[i] + "."
    # Remove the last dot from the result string
    # Slice the String at the end
    return result[:-1]


S = "pqr.mno"
print(reverse_string(S))
