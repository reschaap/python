def isLucky(n):
    array = [int(num) for num in str(n)]
    half = int(len(array)/2)
    return sum(array[:half]) == sum(array[half:])