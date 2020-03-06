
from collections import OrderedDict
from operator import itemgetter

"""
for i in range(0, len(arr)):
    diff= abs(arr[i]-(i+1))
    for x in arr:
      store[i] =diff  
  thank= OrderedDict(sorted(store.items(), key=itemgetter(1)))
  print(thank)
"""

def swapper(arr):
  temp = [0] * (len(arr) +1) #CREATES AN ARR WITH ALL ZEROS, 
  #WITH LEN OF ARR + 1

  for pos, val in enumerate(arr): #creates a key num index, with values for each key
    #print()
    temp[val]= pos #each val in arr is a key of Temp[val], 
    #pos (index) = value of temp arr 
    #print("temp[val]", "val(index)", val,"pos", pos,"tempArr:", temp)
    #pos +=1 # increment index/ arr value in temp arr , #as 
   #temp is created
    swaps = 0
  for i in range(len(arr)):
    if arr[i]!= i+1 :#this condition checks if sorted 
      swaps += 1 #swap increases by 1 
      t = arr[i] # store arr[i](not sorted) in var t! # t=arr[0]=4                     #3=arr[1]
      #print("t0", t)    
      #print("arr[i]", arr[i])      
      arr[i] = i+1 #change value of arr[i] to sorted  # arr[0]= o+1 = 1   
      #print("i:", i, "arr[i] = i+1, arr[i]: ", arr[i],"arr[temp[i+1]]: ", arr[temp[i+1]] )         #arr[1] = 1+1
      arr[temp[i+1]] = t #temp[0+1]=> 3 => arr[3]= t   # arr[temp[0+1] =>3]= t     #arr[temp[1+1]=>2] = t 
      #print("arr[temp[i+1]]: ", arr[temp[i+1]] )
      #print("after arr[temp[i+1]] =t. t= ", t)
      temp[t] = temp[i+1] # temp[3]= temp[0+1] =>  temp[3] = temp[2]  or 1 = 2
      #print("i:", i, "t:", t, "temp[t]:", temp[t], "temp[i+1]:", temp[i+1], "temp:", temp)
  print(swaps)
  return swaps 




#7,1,3,2,4,5,6

#1,3,5,2,4,6,7
  


print(swapper([1,3,5,2,4,6,7]))