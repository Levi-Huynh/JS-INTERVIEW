/*
 * Complete the 'numberOfWays' function below.
 *
 * The function is expected to return a LONG_INTEGER_ARRAY.
 * The function accepts 2D_INTEGER_ARRAY queries as parameter.
 * U
# OF WAYS box can be divided
case 0-1
3x5 =15 ways to choose 1x1 area of cables # row * column, store res in arr
2*4 =8 ways to choose 2x2 area # let min(row, column)=my min===> mymin -1 * ((mmymin-1)*(mymin-1)), store res in arr
1*3 = 3 wasy to choose 3x3 area  #mymin-2 * (mymin-0* mymin-0), store res in arr
sum tgoether res array 
input= 2D array of ints, each represents box dimensions (rows x colu) for a query

case -1
3*5 [n,t]
2*4 [n-1, t-1]
1*3 

case 0
0.1: [2,1] =2 = total ways 1*2
0.2: [2,3]    
            2x3 =6
            1*2 = 2

case 1
    [3,4] =
            dim 1=    12 (3*4)
            dim 2=    6 (2*3)
            dim 3=     2 (1*2)
    [6,5]            
             dim 1=    5*6=30  
            dim 2=     20 (4*5)
            dim 3=     12  (3*4)
            dim 4=     6    (2*3)
            dim 5 =   2     (1*2)
    [6,5]            sum of above

    
P
E
R
 */



function numberOfWays(queries) {
    // Write your code here
    // loop thru i, to access all sub arrays
    //mult query[0][n,m] 
    // m*n, min(n,m) = min 
    //
    // min-track * m-track
    // push to res (m*n, min-i * max-i)
    let res1 = []
    let res4 = []
    let res3 = []
    let res2 = []
    let myo = {}
    let data = []
    for (let i = 0; i <= queries.length; i++) {
        let myMin = Math.min(queries[i][i], queries[i][i + 1])
        let myMax = Math.max(queries[i][i], queries[i][i + 1])
        let myNewMin = myMin - (myMin + 1)



        console.log("I", i)


        for (let j = 1; j <= myMin; j++) {
            console.log("j", j, "i", i)
            res1[i] = {
                val: j * (j + 1)

            }
        }




    }

    console.log("res1", res1)
}


numberOfWays([[3, 4], [6, 5]])