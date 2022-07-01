def binarySearch(arr, target):
    lo, hi = 0, len(arr)-1
    
    while lo <= hi:
        mid = (lo+hi)//2
        if(arr[mid] == target):
            return mid
        if(arr[mid] > target):
            hi = mid-1
        else:
            lo = mid + 1
    
    return -1

if __name__ == "__main__":
    print(binarySearch([1, 2, 4, 6, 8, 10, 15, 17, 19], 17))