class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for i in s:
            if i == "(":
                # An Opening Bracket just put it into the stack and move forward
                stack.append(i)
            else:
                # If the Length of the Stack is zero that means no other bracket was in there
                # We have encountered a closing Bracket without an opening bracket so increase the count
                if len(stack) == 0:
                    count = count+1
            # Invalid closing bracket
                else:
                    stack.pop()

        # To Make sure we are not missing any invalid opening brackets
        return count+len(stack)
