class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_string_builder = []
        strobo = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        for i in (num):
            if i not in strobo:
                return False
            rotated_string_builder.append(strobo[i])
        rotated_string_builder.reverse()
        # I can traverse through the reverse string in the first place to not reverse it at the end
        rotated_string_builder = "".join(rotated_string_builder)
        return rotated_string_builder == num
    '''
        The time complexity of this function is O(n), where n is the length of the input string num.
        This is because the function needs to traverse through all the characters in the input string.
        The space complexity of this function is also O(n)
        since the rotated_string_builder list will use up to O(n) space in the worst case.
    '''

    def isStrobogrammatic(self, num: str) -> bool:
        rotated = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        left = 0
        right = len(num) - 1
        while left <= right:
            if num[left] not in rotated or rotated[num[left]] != num[right]:
                return False
            left = left+1
            right = right-1
        return True


'''
The time complexity of this function is O(n), where n is the length of the input string num.
This is because the function needs to traverse through all the characters in the input string.
The space complexity of this function is O(1), since the loop variables left and right take up a constant amount of space.
'''
A = "69"
ob = Solution()
print(ob.isStrobogrammatic(A))
