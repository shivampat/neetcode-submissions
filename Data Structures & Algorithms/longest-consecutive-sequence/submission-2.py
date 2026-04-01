class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums:
            num_set.add(num)
        
        max_length = 0
        for num in num_set:
            seq_length = 1
            while num+1 in num_set:
                num += 1
                seq_length += 1
            max_length = max(max_length, seq_length)
        
        return max_length

        
