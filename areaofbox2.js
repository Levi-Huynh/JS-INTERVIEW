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
    for (let i = 0; i < queries.length; i++) {

        let myMin = Math.min(queries[i][0], queries[i][1])
        let myMax = Math.max(queries[i][0], queries[i][1])
        //console.log("i", i, myMin, myMax)
        res1[i] = {
            sub: i,
            val: myMin * myMax
        }
        /* if(i==0){
           res3.push(myMax*myMin)
           }else if(i==1){
             res2.push(myMax*myMin)
             }//first way row * dim
             // console.log("res1",res1)
             // res2[i]
   */

        for (let j = myMin - 1; j > 0; j--) { //remaining ways //increment j up 

            let myvar = myMax
            res4.push([j * (j + 1), i])

            console.log(res4)


            // console.log("J",j,"I",i ,"myvar", myvar)
            // res2[i][j]= j* (j+1)

            /*  if(i==0){
                console.log("i", i)
              res3.push(j*(j+1))
              }else if (i==1){
                console.log("i", i)
                res2.push([j*(j+1), i])
              }
             //    console.log("res2", res2)
             */
        }

    }

    //console.log("res1",res1)
    console.log("res1", res1)
    console.log("res4", res4)
    for (let m = 0; m < res4.length + 1; m++) {
        if (res4[m][1])
  }
}


numberOfWays([[3, 4], [6, 5]])