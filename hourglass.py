# Complete the hourglassSum function below.
def hourglassSum(arr):
    result1 = []
    result = {}
    store = []
    # 4 total diff arrays accros
    # 4 total diff arrays down

    # columns: #width, or len of one f the sub_arrays
    # only go up to -2 columns
    for j in range(0, (len(arr[0])-3)):  # j = 0, 1,2,3
        for i in range(0, (len(arr)-3)):
            # starts over, for each new hour glass
            hour_sum = 0
            hour_sum += arr[i][j] + arr[i][j+1]+arr[i][j+2] + \
                arr[i+1][j+1] + arr[i+2][j]+arr[i+2][j+1] + arr[i+2][j+2]
            result1.append(hour_sum)
            result[i+j] = hour_sum

    for k, v in result.items():
        store.append(v)
    print(f"result: {result}")
    #max_res = max(store)
    max_res = max(result1)
    return max_res
