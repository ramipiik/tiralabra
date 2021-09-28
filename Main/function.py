def function():
    usr_input = input('please enter a number: ')
    while True:
        if int(usr_input) < 5:
            usr_input = input('please, enter a value less then 5: ')
        else:
            break
    return usr_input