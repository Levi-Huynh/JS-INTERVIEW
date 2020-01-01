/**
 1) Seperate values of arr into 2 subsets (A & B)
 2) subsets should not have common elements (make one a set unique only) // create unique set for B 
 3) addition of 2 subsets should equal entire input arr 
 4) SUM subset A  > SUM subset B // conditional that checks A >, as move elements A to subset B 
 5) # of elements in subset A = minimal
 6) if mult solutions for A(// compare and return set that has the max total sum of all elements) 
 */

/* 
var fruits = new Array(4).fill('Lemon');
console.log(fruits);

var fruits = Array.from(
  { length: 4 },
  () => ({ Lemon: 'Lemon' })
);

console.log(fruits);
[
  {
    "Lemon": "Lemon"
  },
  {
    "Lemon": "Lemon"
  },
  {
    "Lemon": "Lemon"
  },
  {
    "Lemon": "Lemon"
  }
]
*/


array_elements = ["a", "b", "c", "d", "e", "a", "b", "c", "f", "g", "h", "h", "h", "e", "a"];

array_elements.sort();
arr_num = [20,
    2,
    3,
    4,
    4,
    5,
    9,
    7,
    8,
    6,
    10,
    4,
    5,
    10,
    10,
    8,
    4,
    6,
    4,
    10,
    1]
function sortNum(a, b) {
    return a - b
}
arr_num.sort(sortNum)

function count(arr) {
    var current = null
    var cnt = 0;
    var k = 0;
    var objar = []
    var dupArr = []
    var dupArr1 = []
    var flatdup = []
    var cleanup = []
    var arrSum = []
    var subA = []
    var cleanupSum = []
    var subAsum = []
    var checksum = []
    var subB1 = []
    var subA1 = []


    for (var i = 0; i < arr.length; i++) {
        if (arr[i] != current) {
            if (cnt > 0) {
                objar[i] = {
                    element: current,
                    count: cnt
                }
            }
            current = arr[i];
            cnt = 1; //if not null & not previous, cnt =1!!!
        } else {
            cnt++; // b/c sorted, cnt++ if arr[i] =! whats stored in current (prev arr[i])
        }
    }//loop
    objar.map((currv, i) => {
        if (currv.count > 1) {
            /*dupArr[i] ={
              element: currv.element,
              count: currv.count
            }*/
            dupArr1[i] = new Array(currv.count).fill(currv.element)

        }
    })

    flatdup = [].concat(...dupArr1)
    flatdup.map(curr => {
        if (curr !== undefined) {
            cleanup.push(curr)
        }
    })
    // push currv.elem into arr, elem.count times
    arrSum = arr.reduce((a, b) =>
        a + b)
    arr.map((curr, i, arr) => {

        if (cleanup.includes(curr) == false) {
            subA.push(curr)
        }
    })

    // [ 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 10, 10, 10, 10, 20 ]
    // j=20,19,18, 17
    //
    //HOW TO DIVIDE SO GET THE LARGEST REP FIRST, THEN FIND NEXT LARGEST INT (next largest can be REP OR NON REP, AND JUST PUSH UNTIL SUM AND INTERESECTION IS NULL
    var thing = cleanup.includes(arr_num[arr_num.length - 1])
    arrSum = arr.reduce((a, b) => a + b)

    for (var j = arr_num.length - 1; j >= 0; j--) {  //find way to push when subAsum < cleanupSum && when cleanup value is present in both subarrays

        var sumB = subB1.reduce((a, b) => a + b, 0)
        var sumA = subA1.reduce((a, b) => a + b, 0)
        var test = sumA - sumB
        console.log(subA1, subB1, arr_num[j], test, "j:", j)

        if (arr_num[j] >= arr_num[j - 1] || sumA <= sumB) { // value j+1 > j

            subA1.push(arr_num[j])

            //cleanup.splice(j,1);


        } else {

            subB1.push(arr_num[j])

        }

    }

    console.log("finaL: ", subA1, subB1, arr_num, sumB, sumA, thing, arrSum)
}

//count(array_elements)
count(arr_num)

//array.reduce(function(total, currentValue, currentIndex, arr), initialValue)
//var arr = ['a','b','c','d','d','e','a','b','c','f','g','h','h','h','e','a'];
/*
function redMeth(arr1){

arr1.reduce(function(prev, cur) {
console.log("prev1: ", prev, "cur1: ", cur)
prev[cur] = (prev[cur] || 0) + 1;
console.log("prev2: ", prev, "cur2: ", cur)
return prev;
}, {})

}

console.log("redMeth",redMeth(arr) )
*/

//array.filter(function(currentValue, index, arr), thisValue)

/*

The filter() method creates an array filled with all array elements that pass a test (provided as a function).

Note: filter() does not execute the function for array elements without values.

Note: filter() does not change the original array.
*/

/*
8
8
9
10
10
10
10
*/

/*
20, 7,6,6,5,5,4,4,4,4,4,3,2,1
*/