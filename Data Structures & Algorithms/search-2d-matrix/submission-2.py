class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])

        r,l = 0, rows - 1

        while r <= l:
            row = (r + l) // 2
            if target > matrix[row][-1]:
                r = row + 1
            elif target < matrix[row][0]:
                l = row - 1
            else:
                break
        if not r <= l:
            return False
        
        row = (r + l) // 2

        cr,cl = 0, cols - 1
        while cr <= cl:
            mid = (cr+cl) // 2
            if target > matrix[row][mid]:
                cr = mid + 1
            elif target < matrix[row][mid]:
                cl = mid - 1
            else:
                return True
        return False
