def func(a,c,b):
    if c=='+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=='/':
        return a//b

    return
    
print(func(int(input('Enter your number: ')),input('Enter sign: '),int(input('Enter your number: '))))