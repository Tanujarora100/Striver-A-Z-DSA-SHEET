class Solution:
    # Without using a Map
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            # Push all the opening brackets into the stack
            else:
                if len(stack) == 0:
                    return False
                # No Opening Bracket has been pushed before a closing one so it cannot be balanced
                top_character = stack.pop()
                if top_character == '(' and s[i] == ')' or top_character == '{' and s[i] == '}' or top_character == '[' and s[i] == ']':
                    continue
                else:
                    return False
                # Edge case can be there are no closing brackets and only opening brackets
        return len(stack) == 0
    # If the Length is not zero at the end that means there are some opening brackets present in the stack which do not have a corresponding closing bracket leading to a unbalanced parantheses

    def isValid(self, s):
        stack = []
        valid = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in valid:
                stack.append(char)
            else:
                if len(stack) == 0 or char != valid[stack.pop()]:
                    return False
        return not stack
