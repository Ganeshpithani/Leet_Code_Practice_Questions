class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        f=[]
        for c in range(len(matrix[0])):
            row=[]
            for r in range(len(matrix)):
                row.append(matrix[r][c])
            f.append(row)
        return f
        