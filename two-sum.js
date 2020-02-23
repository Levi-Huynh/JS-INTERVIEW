var twoSum = function (nums, target) {
    let res = 0
    let arr = []
    let ind = []
    for (let x = 0; x < nums.length; x++) {
        for (let j = x + 1; j < nums.length + 1; j++) {
            let test = nums[x] + nums[j]
            console.log(test)
            if (test == target) {
                arr.push(x, j)
            }
        }
    }

    return arr
};


twoSum([2, 11, 7, 15], 9)