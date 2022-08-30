

def OddEvenSum(num):
    evenSum = 0
    oddSum = 0
    for i in str(num):
        if int(i) % 2 == 0:
            evenSum = evenSum + int(i)
        else:
            oddSum = oddSum + int(i)

    return max(evenSum, oddSum)


print(OddEvenSum(274695))