class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list = defaultdict(list)
        for anagram in strs:
            letter_count = [0]*26
            
            for letter in anagram:
                letter_indx = ord(letter) - ord('a')
                letter_count[letter_indx] += 1
            
            anagram_list[tuple(letter_count)].append(anagram)
        
        return anagram_list.values()