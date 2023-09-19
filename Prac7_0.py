import matplotlib.pyplot as plt


def binarySearch(YGN,num,count=0):
    mid  = len(YGN)//2
    
    count += 1
    if (mid == 0 or mid == len(YGN)-1) and not(YGN[mid] == num):
        return -1
    if num == YGN[mid]:
        return count
    elif num < YGN[mid]:
        return binarySearch(YGN[:mid],num,count)
    else :
        return binarySearch(YGN[mid:],num,count)
    
def linearSearch(YGN,num):
    count = 0

    for i in YGN:
        count += 1
        if num == YGN[i]:
            return count
    
    return -1

List1 = list(range(2000))
data = list(range(0,2000,100))

L_count = []
B_count = []

for i in data:
    L_count.append(linearSearch(List1,i))
    B_count.append(binarySearch(List1,i))

print("Data Used : ",data)
print("Linear search count : ",L_count)
print("Binary search count : ",B_count)

plt.plot(data,L_count,marker='x',label='Linear Search',color='Crimson')
for i in range(len(data)):
    plt.annotate(f'{L_count[i]}', (data[i], L_count[i]), textcoords="offset points", xytext=(0,10), ha='center',color='Crimson')

plt.plot(data,B_count,marker='x',label='Binary Search',color='b')
for j in range(len(data)):
    plt.annotate(f'{B_count[j]}', (data[j], B_count[j]), textcoords="offset points", xytext=(0,-15), ha='center',color='b')

plt.title("Linear Search & Binary Search Comparision")
plt.xlabel("Comparison counts")
plt.ylabel("Data Used")
plt.legend()
plt.show()