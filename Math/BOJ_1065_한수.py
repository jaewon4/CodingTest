def is_hansu(N):
    if N < 100:
        return True
    elif N < 1000:
        hundreds = N // 100
        tens = N % 100 // 10
        ones = N % 10
        if hundreds - tens == tens - ones:
            return True
        else:
            return False
    elif N == 1000:
        return False
    else:
        print("error")
        return 0
        
def count_hansu(N):
    count = 0
    for i in range(1, N + 1):
        if is_hansu(i):
            count += 1
    return count

result = count_hansu(int(input()))
print(result)