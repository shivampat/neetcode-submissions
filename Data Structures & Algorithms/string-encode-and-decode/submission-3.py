class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for string in strs:
            encodedStr += f"{len(string)}#{string}"
        print(encodedStr)
        return encodedStr

    def decode(self, s: str) -> List[str]:
        i = 0
        decodedList = []
        while i < len(s):
            wordSize = ""
            word = ""
            while s[i] != '#':
                wordSize += s[i]
                i += 1
            wordSize = int(wordSize)
            i += 1
            for j in range(wordSize):
                word += s[i]
                i += 1
            print(word)
            decodedList.append(word)
        return decodedList
                


