class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {}
        for num in nums:
            num_dict[num+1] = num
        
        max_length = 0
        for num in num_dict.keys():
            seq_length = 1
            while num-1 in num_dict.keys():
                num -= 1
                seq_length += 1
            max_length = max(max_length, seq_length)
        return max_length

        
