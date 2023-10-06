
def printParenthesis(i , j, n, bracket):

    if (i == j):
       print(f'A[{i}]',end='')
       return
     
    print("(", end = "")

    printParenthesis(i, bracket[i][j], n, bracket)

    printParenthesis(bracket[i][j] + 1, j, n, bracket)
    print(")", end = "")
   

def MCM(Dimensions,n):
    m = [[0]*n for _ in range(n)]
    parenthesization = [[0] * n for _ in range(n)]
    for p in range(1, n):
        m[p][p] = 0
    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i+L-1
            m[i][j] = int(1e9+7)
            
            for k in range(i,j):
                steps = m[i][k] + m[k+1][j] + Dimensions[i-1]*Dimensions[k]*Dimensions[j]
                if steps < m[i][j]:
                    m[i][j] = steps
                    parenthesization[i][j] = k
    print('Optimal parenthesization :',end=' ')
    printParenthesis(1,n-1,n,parenthesization)
    return m[1][n-1]


Dimensions = [5, 4,6,2,7]
n = len(Dimensions)
print("\nThe number of scalar multiplications needed : ",MCM(Dimensions,n))