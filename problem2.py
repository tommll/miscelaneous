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
            ans[j][col] = matrix[row][j]
    
    return ans

def rotate_4_item(matrix, x1, y1, x2, y2, x3, y3, x4, y4):
    # print('rotate_4_item:', x1, y1, x2, y2, x3, y3, x4, y4)
    tmp = matrix[x1][y1]
    tmp, matrix[x2][y2] = matrix[x2][y2], tmp
    tmp, matrix[x3][y3] = matrix[x3][y3], tmp
    tmp, matrix[x4][y4] = matrix[x4][y4], tmp
    tmp, matrix[x1][y1] = matrix[x1][y1], tmp

def rotate_4_times_at_index(matrix, n, x0, y0, x, y):
    if n <= 1: return
    if n % 2 != 0 and x == y == (n-1)/2: return

    if x == y:
        x1, y1 = x0 + x, y0 + y
        x2, y2 = x0 + x, y0 + n - 1
        x3, y3 = x0 + n - 1, y0 + n - 1
        x4, y4 = x0 + n - 1, y0 + y
        rotate_4_item(matrix, x1, y1, x2, y2, x3, y3, x4, y4)
    else:
        factor = y + 1
        x1, y1 = x0 + x, y0 + y
        x2, y2 = y1, y0 + n - 1
        x3, y3 = y2, y0 + n - factor
        x4, y4 = y3, y0
        rotate_4_item(matrix, x1, y1, x2, y2, x3, y3, x4, y4)

    return matrix

def rotate_90(matrix, n):
    for i in range(n):
        if n - i * 2 - 1 <= 0:
            break
        else:
            rotateLen = n - i * 2 - 1
            for j in range(rotateLen):
                print(i, i, 0, j)
                rotate_4_times_at_index(matrix, n - i * 2, i, i, 0, j)
    return matrix

matrix = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]
          
print_matrix(rotate_90(matrix, 5))

matrix = [['A', 'B', 'C'],
          ['D','E', 'F'],
          ['G','H', 'I']]
print_matrix(rotate_brute_force(matrix, 3))