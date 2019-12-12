def withdraw():
    print('You choosed to withdraw!!!')
    x = int(input('Enter your amount to withdraw : '))
    if x <= p:
        remaning = p-x
        return remaning
    else:
        print('insufficient balance')

w = withdraw()

print(w)