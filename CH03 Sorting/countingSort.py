def countingSort(arr):
    res = [0] * len(arr)
    
    for num in arr:
        res[num] += 1
        
    return res

if __name__ == "__main__":
    print(countingSort([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 3, 1, 1,1 , 5, 1, 2, 5]))