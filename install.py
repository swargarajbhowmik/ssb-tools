# Importing Modules
import os,time,requests
import os.path
from colorama import Fore, Back, Style

from os import path
if path.exists("ssb-hacks.py")==True:
    print(Fore.RED + 'Error: SSB-Hacks Already Installed!')
    exit()

# Logo
print('-'*50)
print (Fore.GREEN+'''

░█▀▀▀█ ░█▀▀▀█ ░█▀▀█ 　 ▀▀█▀▀ █▀▀█ █▀▀█ █── █▀▀ 
─▀▀▀▄▄ ─▀▀▀▄▄ ░█▀▀▄ 　 ─░█── █──█ █──█ █── ▀▀█ 
░█▄▄▄█ ░█▄▄▄█ ░█▄▄█ 　 ─░█── ▀▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀
''')
print('2021 Hacking Tool Containing 500+ Tools')
print('-'*50)

# Menu
print('Main Menu:')
print('[1] Install')
print('[2] Exit')

# Prompt
userinput = int(input('root@ssbtools> '))

# Checking Prompt
if userinput==2:
    print('Ok Exiting...')
    time.sleep(2)
    os.system('cls')
if userinput==1:
    print('Installing SSB-Tools...')
    installurl = 'https://ivider.ml/ssb-hacks.py'
    r = requests.get(installurl, allow_redirects=True)
    open('ssb-hacks.py', 'wb').write(r.content)
    print('SSB-Tools Downloaded Successfully!')
    os.remove("install.py")
