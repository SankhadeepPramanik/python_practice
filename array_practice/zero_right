#technique name: two pointer technique
def zero_right(arr: list) -> list:
    left = 0
    for r in range(len(arr)):
        if arr[r] != 0:
            arr[left], arr[r] = arr[r], arr[left]
            left += 1
    return arr

a = zero_right([0, 0, 1, 0, 2, 3, 0, 9, 6, 7, 0])
print(a)