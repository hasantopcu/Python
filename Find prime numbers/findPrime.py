def findPrimeNumbers(lb,ub):
    primeNumbers = [1]
    for i in range(lb,ub):
        counter = 0
        for j in range(2,i):
            if i%j != 0:
                counter = counter + 1
        if counter == (i-2):
            primeNumbers.append(i)
            lb = i 
   
if __name__ == "__main__":
    findPrimeNumbers(lower_boundry , upper_boundry)
    
    
    
    
