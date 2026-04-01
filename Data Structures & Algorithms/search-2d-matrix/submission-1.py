class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            m = l + ((r - l) // 2) 

            row = matrix[m]
            first, end = row[0], row[-1]

            if first > target:
                r = m - 1
            elif end < target: 
                l = m + 1
            else:
                break

        l, r = 0, len(matrix[m])-1
        while l <= r:
            rowm = l + ((r - l) // 2)

            num = matrix[m][rowm]

            if num > target:
                r = rowm - 1
            elif num < target:
                l = rowm + 1
            else:
                return True
        
        return False

        
