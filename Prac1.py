params = int(input())
if params < 1:
    print("Enter a valid number")
else:
    chef1 = input("").split(' ')
    chef2 = input("").split(' ')
    c1=0
    c2=0
    for i in range(0,params):
        chef1[i] = int(chef1[i])
        chef2[i] = int(chef2[i])
        if chef1[i] > chef2[i]:
            c1+=1
        else:
            c2+=1

print(c1,c2)