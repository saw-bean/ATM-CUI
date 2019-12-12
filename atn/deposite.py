def deposite():
    dep = 0
    print('You choosed to deposite ')
    depo = int(input('How much you want to deposite??'))
    dep = dep+depo
    return dep
p = deposite()
print(f'your total balance is{p}')



