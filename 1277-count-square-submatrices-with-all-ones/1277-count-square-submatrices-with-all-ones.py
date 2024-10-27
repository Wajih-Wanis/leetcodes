class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        area = 1
        result = 0
        breaker = pow(max(len(matrix),len(matrix[0])),2)
        while area<=breaker:
            mask_result = []
            for i in range(len(matrix)-1):
                temp = []
                for j in range(len(matrix[0])-1):
                    temp.append(matrix[i][j]+matrix[i+1][j]+matrix[i][j+1]+matrix[i+1][j+1])
                mask_result.append(temp)
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j]==area:
                        result+=1
            matrix = mask_result
            area*=4

        return result
        