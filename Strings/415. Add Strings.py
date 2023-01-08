def addStrings(self, num1: str, num2: str) -> str:
        num1 = [eval(i) for i in num1]
        num2=[eval(i) for i in num2]
        num_one_sum=0
        num_two_sum=0
        for i in range(len(num1)):
            num_one_sum=num_one_sum*10+num1[i]
        for i in range(len(num2)):
            num_two_sum=num_two_sum*10+num2[i]
        combined_sum= num_one_sum+num_two_sum
        return str(combined_sum)




def addStrings(self, num1: str, num2: str) -> str:
        numDict = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5,
                  '6' : 6, '7' : 7, '8' : 8, '9' : 9}
        def str2int(num):
            output = 0
            for i in num:
                output = output * 10 + numDict[i]
            return output
        
        return str(str2int(num1) + str2int(num2)) 
    
