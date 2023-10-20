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
	return K[len(profits)][max_W]


profits = [280,100,120,120]
weights = [40,10,20,24]
max_W = 60
print(knapSack(max_W, weights, profits))
