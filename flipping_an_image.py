A = [[1,1,0],[1,0,1],[0,0,0]]
result=[]
for i in A:
    temp = []
    for value in i[::-1]:
        temp.append(1 - value)
    result.append(temp)


print(result)