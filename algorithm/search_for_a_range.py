def bin_search(data_set,value):
    low = 0
    high = len(data_set) - 1
    while low <= high:
        mid = (low + high) // 2
        if data_set[mid] == value:
            a = mid
            b = mid
            while data_set[a] == value and a >= 0:
                a-=1
            while data_set[b] == value and b <= len(data_set)-1:
                b+=1
            return (a+1,b-1)
        elif data_set[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

print(bin_search([1,2,3,3,4,5,6],3))