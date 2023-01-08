class Solution:
    def reverse(self, x: int) -> int:
        flag=False
        if x<0:
            flag=True
        copy_num=abs(x)
        reverse_num=0
        while copy_num:
            rem= copy_num%10
            reverse_num=reverse_num*10+rem
            copy_num=copy_num//10
        #Edge Case
        if reverse_num>=2**31 or reverse_num<= -2**31:
            return 0
        if flag:
            return -(reverse_num)
        else:
            return reverse_num
