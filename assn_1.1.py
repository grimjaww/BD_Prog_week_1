x = input('Add a String: ')
y = input('Add a String for comparision: ')

def lcs(a, b):
    matrix = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                matrix[i+1][j+1] = matrix[i][j] + 1
            else:
                matrix[i+1][j+1] = max(matrix[i+1][j], matrix[i][j+1])
 
    result = ''
    j = len(b)
    for i in range(1, len(a)+1):
        if matrix[i][j] != matrix[i-1][j]:
            result += a[i-1]
 
    return(result)

print(lcs(x,y))