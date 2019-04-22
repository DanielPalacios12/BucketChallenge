def bucketsSum(bucket_sizes, l, target_value):
    total = [0 for k in range(target_value + 1)]
    total[0] = 1
    for k in range(1, target_value + 1):
        for i in range(l):
            if k >= bucket_sizes[i]:
                total[k] += total[k - bucket_sizes[i]]
    return total[target_value]


bucket_sizes1 = input("Enter bucket sizes: ")
bucket_sizes = list(map(int, bucket_sizes1.split()))
target_value = int(input("Enter target value: "))
l = len(bucket_sizes)
if bucketsSum(bucket_sizes, l, target_value) >= 1:
    print(1)
else:
    print(0)
