list = [1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]


NO1 = 0
NO2 = 0

for temp in list:
    if temp > NO1:
        NO1 = temp
        continue
    elif temp > NO2 :
        NO2 = temp

print ('NO1 big is %s,NO2 big is %s' %(NO1,NO2))
        
        

    
