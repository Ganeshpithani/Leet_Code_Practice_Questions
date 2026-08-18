class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        rm={min(row) for row in matrix}
        cm={
            max(matrix[i][j] for i in range(len(matrix)))
            for j in range(len(matrix[0]))
        }
        return list(rm & cm)