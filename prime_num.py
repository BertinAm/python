import time
t0 = time.time()
nums = 2
for i in range(2, nums):
    if nums % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")
t1 = time.time()
print(t1 - t0)