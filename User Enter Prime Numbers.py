while True:
    num = int(input("Enter a Number: "))
    if num<2:
        print('Less than 2. Try Again!!')
        continue
    else:
        isPrime = True
        for i in range(2, num):
            if num%i==0:
                isPrime = False
                break
        if isPrime:
            print(f"{num} is a Prime Number!!")
            break
        else:
            print(f"{num} is not a Prime Number")