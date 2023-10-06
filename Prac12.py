
class Item:
	def __init__(self, profit, weight):
		self.profit = profit
		self.weight = weight

# Main greedy function to solve problem
def fractionalKnapsack(W, arr):
	arr.sort(key=lambda x: (x.profit/x.weight), reverse=True)
	# Result(value in Knapsack)
	profits = []
	weights = []
	Max_profit = 0.0
	ratio = []
	for a in arr:
		profits.append(a.profit)
		weights.append(a.weight)
	for item in arr:

		# If adding Item won't overflow, 
		# add it completely
		if item.weight <= W:
			W -= item.weight
			Max_profit += item.profit
			ratio.append(1)
		# 2,3,4 W = 3 

		# If we can't add current Item, 
		# add fractional part of it
		else:
			Max_profit += item.profit * W / item.weight
			ratio.append(round(W/item.weight,2))
			break
	if len(ratio) != len(weights):
		ratio.append(0)
	print("Profits : ",profits)
	print("weights : ",weights)
	print("Ratio :",ratio)
	print("maxProfit :", Max_profit)



profits = list(map(int,input("Enter the Profits : ").split(' ')))
weights = list(map(int,input('Enter the weights : ').split(' ')))
Cap = int(input("Enter max weight :"))

PW = [Item(profit, weight) for profit,weight in zip(profits,weights)]
# Function call

fractionalKnapsack(Cap, PW)
