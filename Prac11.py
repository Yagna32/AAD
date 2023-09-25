def knapSack(max_W, wt, profits):
	K = [[0 for x in range(max_W + 1)] for x in range(len(profits) + 1)]

	for i in range(len(profits) + 1):
		for w in range(max_W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i-1] <= w:
				K[i][w] = max(profits[i-1]+ K[i-1][w-wt[i-1]],K[i-1][w])
			else:
				K[i][w] = K[i-1][w]
	for j in K:
		print(j)
	return K[len(profits)][max_W]


profits = [3,4,5,6]
weights = [2,3,4,5]
max_W = 5
print(knapSack(max_W, weights, profits))
