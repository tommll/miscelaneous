def print_matrix(matrix):
    for row in matrix:
        print(row)


def rotate_brute_force(matrix, n):
    ans = []
    for row in matrix:
        ans.append(row.copy())
    
    for row in range(n):
        for j in range(n):
            col = n - 1 - row
            print(row, j , 'to', j, col)
            ans[j][col] = matrix[row][j]
    
    return ans


matrix = [['A', 'B', 'C'],
          ['D','E', 'F'],
          ['G','H', 'I']]
print_matrix(rotate_brute_force(matrix, 3))