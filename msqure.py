""" 

 
  Mag Square 
  #always do Detective work nm what
UNDERSTAND
-nxn matrix of distinctive pos INT from 1 to n^2 
-Sum of any row, column, or diagonal of length n is always equal to the same 
number: "Mag" constant
-Given: 3x3 matrix s of integers in the inclusive range [1,9]
we can convert any digit a to any other digit b in the range [1,9]
at cost of |a-b| 
-Given s, convert it into a magic square at minimal cost.  Print this cost to a new line
-constraints: resulting magic square must contain distinct integers on inclusive range [1,9]

input= array (3x3 matrix) of s intes, in range[1,9] (convert any digit a to any digit b in range [1,9] at cost |a-b| abs value a-b)

output= minimal cost |a-b|, 1 integer

input:
5* 3 4
1 5 8*
6 4* 2

OUTPUT:
8* 3 4
1 5 9* 
6 7* 2

input [[5,3,4],[1,5,8],[6,4,2]]
          12     14      12 
output [[8,3,4],[1,5,9],[6,7,2]]
          15      15      15

if [i][i]  +  [i+1][i]  +     [i+2][i]  //C
  [i][i] + [i][i+1] + [i][i+2] && //R
   [i][i] + [i+1][i+2] + [i+2][i+2] //D  

   
         
oputput took 3 replacements at cost of |5-8| + |8-9| + |4-7| = 7 
                                        3        1      3
row, column, diagonal

row1 = s[0][0] [0][1] [0][2]
2 = s[1][0], [1][1], [2][2]
3    [2][0]   [2][1]    [2][2]
 
 #i do it the way you want it done, when you want it done lord
 #when i say i dont have money for something you ask me for, lack of faith  
 # do you help me to your own hurt? put me first  

#my strength is in you your laws ty, consistently give all the time 

input: 
4 8* 2   |9-8| 1     // 14R, 15D, 14C
4* 5 7    |3-4| 1   // 16RM, 14MC
6* 1 6   |8-6|  2  //  13R, 13D, 15C

input [[4,8,2],[4,5,7],[6,1,6]]
        14       16      13  
output [[4,9,2],[3,5,7],[8,1,6]]
          15      15       15
totla min =4 

PLAN

EXECUTE


REFLECT


 */


/*
input:
5* 3 4
1 5 8*
6 4* 2

OUTPUT:
8* 3 4
1 5 9* 
6 7* 2

input [[5,3,4],[1,5,8],[6,4,2]]
          12     14      12 
output [[8,3,4],[1,5,9],[6,7,2]]
          15      15      15

if [i][i]  +  [i+1][i]  +     [i+2][i]  //C
  [i][i] + [i][i+1] + [i][i+2] && //R
   [i][i] + [i+1][i+2] + [i+2][i+2] //D  


 */

function Sq(arr) {

let i = 0;

  let col1 = arr[i][i]  +  arr[i+1][i]  +  arr[i+2][i]
  let col2 = arr[i][i+1]  +  arr[i+1][i+1]  +  arr[i+2][i+1]
  let col3 = arr[i][i+2]  +  arr[i+1][i+2]  +  arr[i+2][i+2]

  let row1 =  arr[i][i] + arr[i][i+1] + arr[i][i+2]
  let row2 = arr[i+1][i] + arr[i+1][i+1]+ arr[i+1][i+2]
  let row3=arr[i+2][i] + arr[i+2][i+1]+ arr[i+2][i+2]
  
  let dia = arr[i][i] + arr[i+1][i+1] + arr[i+2][i+2] 
  let dia2 = arr[i][i+2] + arr[i+1][i+1] + arr[i+2][i]

//console.log("col1:", col1, "col2:", col2, "col3:", col3+ "\n" + "row1:", row1,  "row2:", row2, "row3:", row3  + "\n" + "diag:", dia, "diag2:", dia2)

console.log(col1 - col3)
}

Sq([[5,3,4],[1,5,8],[6,4,2]])
//

//1=? what makes the col/row/diag thats not the primary sums, equal to primary sum

//2== how to find the col/row/diag thats diff than main prim sum
// store all sums of each col/rows/diags in list
// find most freq sum 
// if col/row/diag != mostfreqsum, then store in tracker array diffSum=[]
//diffSum 14, 14
// mostfreqsum - each tracker:colX/rowX/diagX
// store ^ all difference in track variable 


col1: 12 col2: 12 col3: 14
row1: 12 row2: 14 row3: 12
diag: 12 diag2: 15


"""

import statistics

def Sq(arr):
  i=0
  store=[]
  dict1 = {}
  keys = ["col1", "col2",  "col3",  "row1",  "row2",  "row3", "diag",  "diag2"]

  col1 =  arr[i][i]  +  arr[i+1][i]  +  arr[i+2][i]
  col2 = arr[i][i+1]  +  arr[i+1][i+1]  +  arr[i+2][i+1]
  col3 = arr[i][i+2]  +  arr[i+1][i+2]  +  arr[i+2][i+2]
  row1 =  arr[i][i] + arr[i][i+1] + arr[i][i+2]
  row2 = arr[i+1][i] + arr[i+1][i+1]+ arr[i+1][i+2]
  row3=arr[i+2][i] + arr[i+2][i+1]+ arr[i+2][i+2]
  dia = arr[i][i] + arr[i+1][i+1] + arr[i+2][i+2] 
  dia2 = arr[i][i+2] + arr[i+1][i+1] + arr[i+2][i]
  print("col1:", col1, "col2:", col2, "col3:", col3, "\n" + "row1:", row1,  "row2:", row2, "row3:", row3, "\n" + "diag:", dia, "diag2:", dia2)

  store.append([col1, col2, col3, row1,row2, row3, dia, dia2])
  for i in keys:
    for x in store[0]:
      dict1[i] = x
  t= dict1["col1"]
  #print("dict", t)
  counter =0
  num = store[0][0]

  track={}
  for key,value in dict1.items():
    if value not in track:
      track[value]=0
    else: 
      track[value]+=1
  mostfreq= max(dict1, key=lambda k:dict1[k])
  maxtra= max(track, key=track.get)
  print("h",mostfreq,maxtra)
  # if store.count(num) < 3, get average from list
  # FIND mean of store
  """
  mything= sorted(store[0])
  print(mything)
  mymean= statistics.median(mything)
  rmean= round(mymean)
  print(mymean, rmean)


  myl= [rmean-x for x in store[0] if x != rmean]
  mysum= abs(sum(myl))
  print(myl, mysum)
  """
  #return mysum




Sq([[4,9,2],[3,5,7],[8,1,5]]) #1 