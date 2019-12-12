def main():
    def call_this():
        print(f'Welcome to ATM INTERFACE system ,{name}')
        print("choose operation")
        print('1. Assign new pin')
        print("2. pin change")
        print('3. deposite')
        print('4. withdraw')
        print('5. balance inquiry')
        sel = int(input("-"))
        return sel

    in1 = call_this()

    if in1 == 1:
        import new_pin
    elif in1 == 2:
        import pin_change
    elif in1 == 3:
        import deposite
    elif in1 == 4:
        import withdarw
    else:
        print('invalid option')
main()