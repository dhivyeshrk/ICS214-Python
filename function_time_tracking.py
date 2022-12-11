import time
def countToN(n):
    i = 0
    while i<n:
        i+=1
def fun(n):
    print(n)
startTime = time.time()
countToN(1000000)
endTime = time.time()
timeElapsed = endTime - startTime
# print(countToN.__closure__ )
print(f"Total execution time is {timeElapsed:.5f}")

        
    