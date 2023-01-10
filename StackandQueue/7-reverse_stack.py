class Solution:
    def reverse(self, st):
        if len(st) == 0:
            return
        insertion_element = st[-1]
        st.pop()
        self.reverse(st)
        self.insert_at_bottom(st, insertion_element)

    def insert_at_bottom(self, st, element):
        if len(st) == 0:
            st.append(element)
            return

        temp = []

        while st:
            temp.append(st[-1])
            st.pop()
        st.append(element)

        while temp:
            st.append(temp[-1])
            temp.pop()


stack = Solution()
A = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
stack.reverse(A)
print(A)
