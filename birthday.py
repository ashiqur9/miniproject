import ast

birthday = {}
while True:
    try:
        file = open('bday.txt', 'r')
        birthday = file.read()
        birthday = ast.literal_eval(birthday)
        file.close()

    except:
        FileNotFoundError
    name = input('Enter Name to Find Birthday to blank to quit\n')
    if name == '':
        quit()

    else:
        if name.lower() in birthday.keys():
            print('The birthday of ' + name + ' is ' + birthday[name.lower()])
        else:
            print('I can\'t find in database ')
            bday = input('Enter the birthday of' + ' ' + name+'\n')
            birthday[name.lower()] = bday
            file=open('bday.txt','w')
            file.write(str(birthday))
            file.close()
            print('Data is updated')
