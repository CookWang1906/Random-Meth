#status: completed
#No matter how big your number is, it will always go back to 4 2 1
n = int(input('Please input your number here: '))
while n < n*n:
    if n % 2==0:
        n = n/2
        print('Down', n)
    else:
        n = n*3 + 1
        print('Up', n)
    if n == 1:
        break
