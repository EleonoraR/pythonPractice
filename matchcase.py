while True:
    user_input = input("enter county:")
    user_input = user_input.strip()

    match user_input:
        case 'ukraine':
            print("pruvit")
        case 'canada':
            print('hello')
        case 'exit':
            break
        case _:
            print('Hey, you entered unknown command')
print('Bye')
