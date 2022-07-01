def mergesort(arr):
    if(len(arr) > 1):
        mid = (len(arr))//2
        right = arr[:mid]
        left = arr[mid:]

        mergesort(left)
        mergesort(right)
        
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if(left[i] <= right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1 
        print(arr)

if __name__ == "__main__":
    arr = [2,6,1,3,67,8,3,6,12]
    mergesort(arr)
    print((arr))