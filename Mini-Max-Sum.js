/*
HACKERRANK
given 5 pos integers, find min & max that can be calculated by summing exactly
four of the 5 integers.  Print respective min & max values as single line of 2 space seperated long integers

arr = [1,3,5,7,9]
maxSum = 3+5+7+9=24
minSum = 1+3+5+7=16
https://stackoverflow.com/questions/29044427/javascript-how-do-i-return-two-values-from-a-function-and-call-those-two-variab
(minSum, maxSum)

input= arr
output = arr w/ 2 integers or, 2 integers (minSum(arr), maxSum(arr))

 */

function minMaxSum(arr) {
    //sort arr
    // minSum = sum(Arr[0]-arr[3])
    //maxSum = summ(Arr[1]- arr[4])
    let res = []
    let sorted = arr.sort()
    let minSum = 0
    let maxSum = 0
    //length =5
    for (let i = 0; i < arr.length - 1; i++) {

        minSum += arr[i]
        maxSum += arr[i + 1]
        console.log(arr[i], arr[i + 1])

    }
    res.push(minSum, maxSum)
    console.log(res[0], res[1]) //to print to console for hackerrank
    return res
}

minMaxSum([1, 2, 3, 4, 5])