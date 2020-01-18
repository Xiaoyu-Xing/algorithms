class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """

    def multiply_naive(self, A, B):
        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):  # for each row in A
            for j in range(len(B[0])):  # for each column in B
                for k in range(len(A[0])):  # for each element in A's row and B's column
                    result[i][j] += A[i][k] * B[k][j]
        return result

    def multiply_improve(self, A, B):
        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):  # for each row in A
            for k in range(len(A[0])):  # for each element in A's row and B's column
                if A[i][k] == 0:
                    # benefit of switching the loop sequence is that the A[i][k] is known before last loop
                    # skip if 0 for sparse matrix can save lot of time to O(n**2)
                    continue
                for j in range(len(B[0])):  # for each column in B
                    result[i][j] += A[i][k] * B[k][j]
        return result

    def multiply(self, A, B):
        # Preprocess the sparse matrix B, only get the non-zero indices of element in B
        B_processed = [[j for j in range(len(B[0])) if B[i][j] != 0] for i in range(len(B))]
        # print(B_processed)
        result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
        for i in range(len(A)):  # for each row in A
            for k in range(len(A[0])):  # for each element in A's row and B's column
                if A[i][k] == 0:
                    # benefit of switching the loop sequence is that the A[i][k] is known before last loop
                    # skip if 0 for sparse matrix can save lot of time to O(n**2)
                    continue
                for j in B_processed[k]:  # because of preprocessing, no need to loop each element in B's row, only need to loop availabel indices
                    result[i][j] += A[i][k] * B[k][j]
        return result
