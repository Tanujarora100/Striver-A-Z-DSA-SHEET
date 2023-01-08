    def getConcatenation(self, nums: List[int]) -> List[int]:
        merged_array=[]
        length= len(nums)
        for i in range(2*len(nums)):
            merged_array.append(nums[i%length]
        return merged_array
