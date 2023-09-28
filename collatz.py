def colatz(n):
    try:
        no = []
        while n != 1:
            if n % 2 == 0:
                n = n // 2  
                no.append(n)
            else:
                n = 3 * n + 1
                no.append(n)
        print(no)
    except TypeError:
        print('You must put an integer.')
colatz(int(input('Enter number: ')))