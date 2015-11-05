sort_list = [8,34,5,22,1,22,555,2,55,34]
print (sort_list)
len_num = len(sort_list)
for i in range(1,len_num):
    j = i
    temp = sort_list[i]
    while j > 0 and temp < sort_list[j - 1]:
        sort_list[j] = sort_list[j - 1]
        j -= 1
        
    sort_list[j] = temp
    print (sort_list)
print (sort_list)
        
