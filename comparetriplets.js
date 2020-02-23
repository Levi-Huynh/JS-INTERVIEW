function compareTriplets(a, b) {
    let score = [0, 0] //initiate score 

    for (let i = 0; i < a.length; i++) {

        if (a[i] > b[i]) {
            score[0] += 1
        } else if (a[i] < b[i]) {
            score[1] += 1
        }

    }
    return score
}
compareTriplets([17, 28, 30], [99, 16, 8])

https://www.hackerrank.com/challenges/compare-the-triplets/problem
      /*""
input: arr a, arr b (2 arrays)

output: score arr with 2 integers (aScore, bScore)

"*/