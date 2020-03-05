/**
 * 
 -focus on using uper to interivew prep asmap for 1 mo (upsolve,(learn new methods) 4-5 HR probs a day)
U
(front start= 1), increment =1, n = end
- inside queue, anybody, can bribe person in front(towards start), to swap
-a number can only be swapped twice 
-if 2 people swap (original index stickers are still carried)

-GIVEN: current que, find the  _minimum_ number of SWAPS that occured to get que to current state

-OUTPUT; integer, = min number of bribes necessary or print, if 
current state has a number had to be swapped more than twice print" too chaotic"
 
-INPUT: array (of integers) final state of que 
P
E
R
 * 
 */

function minBribe(arr) {
    /*
    -find sorted version of arr 
    -call the index of sorted array i 
    -call the index of unsorted j 
    
    -[2,1,5,3,4] (current state)arr
    -1,2,3,4,5 j 
    - if arr[j] > j ==> entry has moved, use entry 
        - res.push((arr[j]-j))
    -return res?
    - if j < i  ==> not moved  
    - if i-j (start j & i at 1), if at i = 3, & j=5,  abs(j-i => 5-3) = 2  abs(j-i => 2-1)=1 2+1 ==3  https://codereview.stackexchange.com/questions/217867/new-year-chaos-javascript-needs-to-be-sped-up
     */
    let result = []
    let sum = 0
    let mystr = ''

    for (let j = 0; j < arr.length; j++) {
        //console.log("here",j+1, arr[j])
        // console.log("j", j)
        let diff = (arr[j] - 1) - j

        if (diff > 2) {
            mystr = 'Too chaotic'
            return mystr
        }
        let myvar = Math.max(0, arr[j] - 2)
        //console.log("arr[j]", arr[j])

        for (let i = myvar; i < j; i++) {
            //i will always start at either 0, or arr[j]-2 (2 is max j can be at), to range less than j 
            //if arr[i] in second loop, is > arr[j] old loop 
            //i = 0=>1, 1=>3, 4=>7, 2=>7 
            /////console.log("start", myvar, "end", j, "i", i, "arr[i]", arr[i], "arr[j]", arr[j])
            if (arr[i] > arr[j]) {
                sum += 1

            }
        }
    }

    return sum

}
//1,2,3,4,5 
minBribe([1, 2, 5, 3, 7, 8, 6, 4])

    //[2,5,1,3,4]
    //[2,1,5,3,4]
    //[1, 2, 5, 3, 7, 8, 6, 4]
    //[1,2,3,4,5,6,7,8]
    //whats RT of map? 