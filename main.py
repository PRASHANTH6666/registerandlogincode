def register():
    name=input('\nusername:')
    name_format='[^0-9$@_][\w]{1,20}@[a-zA-Z]{5}.[a-z]{2,3}'
    if (re.match(name_format,name)):
        password=input('enter password:')
        password_format='^(?=.*[a-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{5,16}$'
        if(re.match(password_format,password)):
            print('\npaswword accepted')
            file=open('user_details.txt','a')
            file.write(name+','+password+'\n')
            file.close()
        else:
            print('\nmaximum length of password should be 5 to 16 must have one uppercase and one lowercase and one special character')
            register()
    else:
        print('user doesnot start with special character or number\n please enter valid useername')
        print('invalid username the format sholud be e.g:abc234@org.com')
        register()

def login():
    print('\nplease provide details:')
    name=str(input('\nname:'))
    password=str(input('\npassword:'))
    with open('user_details.txt') as ud:
        content = ud.read()
        status=0
        if name in content:
            print('\nwelcome Back, '+ name)
            print('\nlogout press 1')
            option=int(input('option: '))
            if option==1:
                print('\nsuccessfully logged out.....')
                menu()
            else:
                print('\npassword entered is wrong')
                print('\n forget password\n 2. for re_entering password\n')
                res=int(input('please enter the option:'))
                if res==1:
                    register()
                elif res==2:
                    login()
        else:
            print('\nname not found. please register first')

def menu():
    print('\nwelcome\n 1. register\n 2.login\n 3.exit\n')
    option=int(input('enter option:'))
    if option == 1:
        register()
        print('\nregistered successfully')
        menu()
    elif option == 2:
        login()
        menu()
    elif option == 3:
        print('thank you')
    else:
        print('\nplease select the option from menu\n')
        menu()

import re
menu()