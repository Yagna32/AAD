def MCM(Dimensions,n):
    m = [[0]*(n)]*(n)
    for L in range(2,n):
        for i in range(1,n-L+1):
            j = i+L-1
            min_steps = float('inf')
            for k in range(i,j):
                steps = m[i][k] + m[k+1][j] + Dimensions[i-1]*Dimensions[k]*Dimensions[j]
                if steps < min_steps:
                    min_steps = steps
    return m
Dimensions = [1,2,3,4]
n = len(Dimensions)
print(MCM(Dimensions,n))