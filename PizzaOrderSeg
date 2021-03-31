lst = [-11,-8,9,4,5,-6]
size = 3
lst1 = []
j= 0
while size <= len(lst):
    print("Size of the set",size)
    print("Start point",j)
    for i in range(j,size):
        flag = "N"

        if lst[i] < 0:
            print(lst[i])
            lst1.append(lst[i])
            flag = "Y"
            size = size + 1
            j = j+1
            print("Less than 0")
            break
        if i == size-1 and flag != "Y":
            lst1.append(0)
            size = size + 1
            j = j+1
            break
        print("I am here ",i)
