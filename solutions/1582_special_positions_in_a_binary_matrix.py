class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        size_mat = len(mat)
        count = 0
        i = 0
        while i < size_mat:
            if mat[i].count(1) == 1:
                j = mat[i].index(1)
                aux = 0
                for k in range(size_mat):
                    if mat[k][j] == 0:
                        aux += 1
                if aux == size_mat - 1:
                    count += 1
            i += 1
        return count
