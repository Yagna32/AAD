import matplotlib.pyplot as plt

clientsL = list(map(int,list(input("Enter number of clients for loop: ").split(' '))))
clientsE = list(map(int,list(input("Enter number of clients for Equation: ").split(' '))))
clientsR = list(map(int,list(input("Enter number of clients for Recursion: ").split(' '))))

countloop = []
countRecursion = []
countEquation = []

def sumRecursion(n,count=0):
    count+=1
    if not n==0:
        return sumRecursion(n-1,count+1)
    else:
        return count

for i in range(len(clientsL)):
    countL = 0
    countR = 0
    countE = 0

    for j in range(clientsL[i]):
        countL+=1

    Equation = clientsE[i]*(clientsE[i] + 1)/2
    countE = 1

    countR = sumRecursion(clientsR[i])

    countloop.append(countL)
    countEquation.append(countE)
    countRecursion.append(countR)
    
print(countloop,countEquation,countRecursion)

plt.plot(clientsL,countloop,c='c',label="Loop")
plt.plot(clientsR,countRecursion,c='r',label="Recursion")
plt.plot(clientsE,countEquation,c='b',label="Equation")
plt.legend()
plt.show()