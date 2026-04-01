class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1
        
        buckets = [[] for i in range(1+max(freqs.values()))]
        for num, freqs in freqs.items():
            buckets[freqs].append(num)
        
        output = []
        while True:
            for i in range(len(buckets)-1, -1, -1):
                for num in buckets[i]:
                    output.append(num)

                    if len(output) == k:
                        return output
                    


        