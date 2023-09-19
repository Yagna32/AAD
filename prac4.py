import matplotlib.pyplot as plt

n = list(input("enter numbers : ").split(' '))
n = list(map(int,n))

IterCount = []
RecursionCount = []

def iterfibonnacci(n):
    a=0
    temp = 0
    b = 1

    for i in range(n):
        temp = b
        b+= a
        a = temp
    return i
    
    


def fibonacci(n,count=1):
    if n==0 or n==1:
        return count
    return fibonacci(n-1,count+1) + fibonacci(n-2,count+1)


    
for i in range(len(n)):
    RecursionCount.append(fibonacci(n[i]))
    IterCount.append(iterfibonnacci(n[i]))
print("Recusrion Count : " , RecursionCount,"\nIteration count : " , IterCount)

plt.plot(n,IterCount,c='c',label="Loop")
plt.plot(n,RecursionCount,c='r',label="Recursion")
plt.legend()
plt.show()