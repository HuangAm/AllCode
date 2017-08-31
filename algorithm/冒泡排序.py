
def bubble_sort(li):
    for i in range(len(li) - 1): #i是趟
        for j in range(len(li) - i -1): #j是指针
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]
    return li

def bubble_sort_1(li):
    for i in range(len(li) - 1): #i是趟
        exchange = False
        for j in range(len(li) -i -1): #j是指针
            if li[j] > li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]