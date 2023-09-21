# Dynamic Programming implementation of LCS problem

def lcs(X, Y, m, n):

	elements = []
	L = [[0]*(n+1) for i in range(m+1)]
	print(L)
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1]+1
				elements.append([i,j])
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])

	index = L[m][n]
	Lcs_char = [""] * (index+1)
	Lcs_char[index] = ''

	p=m
	q=n
	
	while p>0 and q>0:
		if X[p-1] == Y[q-1]:
			Lcs_char[index-1] = X[p-1]
			p -= 1
			q -=1
			index -= 1
		elif L[p-1][q] > L[p][q-1]:
			p -=1
		else : 
			q -=1
	
	print("\nX : " + X + "\nY : " + Y)
	print("\nLength of LCS is", L[m][n])
	print("\nLCS : " + "".join(Lcs_char))
	print()

	return L[m][n]


S1 = "AGGTAB"
S2 = "GXTXAYB"
m = len(S1)
n = len(S2)
lcs(S1,S2,m,n)
