/*
Given square matrix, calc diff between sum & its diagonals

123
456
989

1+5+9 = 15
3+5+9 =17
|15-17| -2

input = ar
output= abs difference of (sum primary diagonal) & (sum secondary diagnoal ) 



11 2 4   5
4  5 6   4
10 8 -12 8 
12, 2, 4, 5

diag A = 11,5,-12, 5 //9
diag B = 5, 6, 8, 12 //31

length =4

[[11,2,4,5],[4,5,6,4],[10,8,-12,8], [12, 2, 4, 5]
//0,        5           10              15
//      3     6      9         12
    */

function diagonalDifference(arr) {
    // Write your code here
    /*for(let i =0; i<arr.length; i++){
      diagA.push(arr[0]+arr[4]+arr[8])
      diagB.push(arr[2]+arr[4]+arr[6])
    }*/
    let row = arr[0].length
    let diagA = 0
    let diagB = 0
    let track = row
    console.log(row)
    for (let i = 0; i < row; i++) {
        track -= 1
        diagA += arr[i][i]
        diagB += arr[i][track]

        //console.log(diagA, "arrA: ", arr[i][i],  diagB, "arrB: ", arr[i][track])
        //diagA += arr[rTrack][rTrack]+arr[rTrack+1][rTrack+1]+arr[2][2]
        //diagB+= arr[0][3]+arr[1][2]+arr[2][1]+ arr[3][0]
    }
    //console.log(row) 

    //console.log(diagA, diagB, track)
    let absum = Math.abs(diagA - diagB)
    return absum
}

diagonalDifference([[11, 2, 4, 5], [4, 5, 6, 4], [10, 8, -12, 8], [12, 2, 4, 5]])


