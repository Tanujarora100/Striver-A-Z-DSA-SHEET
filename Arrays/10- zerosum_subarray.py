class solution:
    def subArrayExists(self, arr, n):
        sum_reg = set()
        sum_reg.add(0)
        maxi = 0
        for i in range(n):
            maxi = maxi+arr[i]
            if maxi in sum_reg or maxi == 0:
                return True
            else:
                sum_reg.add(maxi)
        return False

    def subArrayExists(self, arr, n):
        maxi = 0
        for i in range(n):
            for j in range(i+1, n):
                maxi = maxi+arr[j]
                if maxi == 0:
                    return True
        return False

    if __name__ == '__main__':
        A = [4, 2, -3, 1, 6]
