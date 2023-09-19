num = input('Enter number of input').split(' ')
num = list(map(int,num))

smallest = abs(num[0] + num[1])
nums = []
for i in range(0,len(num)-1):
    for j in range(i+1,len(num)):
        if abs(num[i] + num[j])<smallest:
            smallest = abs(num[i] + num[j])
        
for A in range(0,len(num)-1):
    for B in range(A+1,len(num)):
        if abs(num[A] + num[B])==smallest:
            nums.append([num[A],num[B]])
        


print(nums)