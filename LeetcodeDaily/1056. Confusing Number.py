class Solution:
    def confusingNumber(self, n: int) -> bool:
        invert = {0: 0, 1: 1, 6: 9, 9: 6, 8: 8}
        inverted_number = 0
        copy_number = n
        while copy_number:
            rem = copy_number % 10
            if rem not in invert:
                return False
            inverted_number = inverted_number*10 + invert[rem]
            copy_number //= 10
        # print(inverted_number)
        if inverted_number == n:
            return False
        return True
