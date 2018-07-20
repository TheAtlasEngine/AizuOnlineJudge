def solve(leftIndex, array, number):
    if number == 0:
        return True
    if leftIndex >= len(array):
        return False
    return solve(leftIndex + 1, array, number) or solve(leftIndex + 1, array, number - array[leftIndex])


n = int(input())
array = list(map(int, input().split()))
q = int(input())
numbers = list(map(int, input().split()))

for number in numbers:
    if solve(0, array, number):
        print("yes")
    else:
        print("no")
