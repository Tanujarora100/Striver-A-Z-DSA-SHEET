class solution:
    def reverse_array(self, arr):
        if (len(arr) == 0):
            return None
        start = 0
        end = len(arr)-1
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr

    def reverseList(self, A, start, end):
        if start >= end:
            return
        A[start], A[end] = A[end], A[start]
        self.reverseList(A, start+1, end-1)


A = [1, 2, 3, 4, 5, 6]
print(A)
obj = solution()
obj.reverseList(A, 0, len(A)-1)
print(A)
