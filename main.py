import os
os.system('cls' if os.name == 'nt' else 'clear')
choise = '''
Another Tools For Make Your Jobs Easier Python Version
--------------------------------------------------------------
- 1) Remote Downloads
- 2) Coloud Downloads
- 3) Shell Finder
- 4) Xml Creator
- 5) Wordpress Find Installation
----------------------------------------------------------------
'''

print(choise)
choice = input('Enter Your Choice : ')

if choice == '1':
    from Scripts import remote
elif choice == '2':
    from Scripts import cloud
elif choice == '3':
    from Scripts import shell
elif choice == '4':
    from Scripts import xmlcreator
elif choice == '5':
    from Scripts import wordpressfind
else:
    print("Wrong Choice")