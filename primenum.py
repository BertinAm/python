number = [1,2,3,4,5,6,7,8,9,10]
for n in number:
    for i in range(2,int(n/2)):
        if n % i == 0:
            print(True , n)
            break
    print(False,n)
            
        
        