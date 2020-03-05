/*
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

U
-Unsorted  arr, consecutive INTS [1,2,3,..n], 
-no duplicates 
-Can only swap any 2 elements  
-Min swaps required to sort array in ascending** 
 Ex:  
 arr=[7,1,3,2,4,5,6]

 input= arr Unsorted INTS
  
output = INT, min number of swaps to sort arr  



p
-iterate thru array, 
-if left < right, swap 
  -make sure it covers all 
- track swap  

E   

R


 */

function swapper(arr){
let swap=0
let store={}
let sorted =[]
let res=[]
//subratct arr[i] from i   
//store subtraction in temp arr 

//index of sorted, temp array will give order that swaps take place
//store sub results in object 
//https://www.codecademy.com/forum_questions/50c207bd55df51ff27004775
//go to original array, 
//sort temp arr of objects   
// swap, based temp index order until sorted  
// stop when condition of arr.sort() == arr   
//ed, & swap with its "value"/ true index  
// swap (0,3)
// check if sorted 
//repeat until all sorted 
//res= arr 
console.log(arr)
for(let i=0; i<arr.length; i++){
  let diff= Math.abs(arr[i]-(i+1)) 
  store[i]={
    "diff": diff, "index": i, "value": arr[i]
  }
}

for(var myind in store){
  sorted.push(store[myind])
}

sorted.sort(function(a,b){

return (a.diff - b.diff);

})
sorted.reverse()//sort to descendig 
console.log("sorted", sorted )

//console.log("store", sorted)

//given sorted 
//take index 0 in sorted, & swap with its "value"/ true index  
// swap (0,3)
// check if sorted 
//repeat until all sorted 
//https://stackoverflow.com/questions/4011629/swapping-two-items-in-a-javascript-array

for(let j=0; j<Object.keys(sorted).length; j++){
//console.log("arr3", arr,arr[store[j].diff], arr[j])


function lilswap(arr){
     var tmp = arr[sorted[j].index];
     console.log("here", arr[sorted[j].index],sorted[j].value-1 )
    arr[sorted[j].index]=  arr[sorted[j].value-1];
    arr[sorted[j].value-1] = tmp;
 
  swap+=1
 //console.log("tmp", arr[j],  arr[sorted[j].diff], j)
} 
lilswap(arr)
console.log("swapped", arr)
}

console.log("end", arr,swap)
}

swapper([4,3,1,2])