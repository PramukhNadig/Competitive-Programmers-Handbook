
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-1):
            if(arr[j] > arr[j+1]):
                swap(arr, j, j+1)
    return arr
def swap(arr, x, y):
    tmp = arr[y]
    arr[y] = arr[x]            
    arr[x] = tmp
    
if __name__ == "__main__":
    arr = [2,6,1,3,67,8,3,6,12]
    print(bubblesort(arr))