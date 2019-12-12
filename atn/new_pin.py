def pin():
    pin = int(input('enter your new pin'))
    if pin<=9999 and pin>999:
        return f'your new pin is :{pin}'
    else:
        return 'pin should be of 4 digit and cannot be string'


x = pin()

print(x)