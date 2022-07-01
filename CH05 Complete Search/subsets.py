from collections import deque
import time

lst = deque()
n = 30
def method1(k=0):
    if(k == n):
        #do somethign
       # print(lst)
        pass
    else:
        method1(k+1)
        lst.appendleft(k)
        method1(k+1)
        lst.popleft()
    

if __name__ == "__main__":
    now = time.time()
    
    print(time.time() - now)