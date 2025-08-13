import os
import sys
import time
import requests
import uuid
import random
import string
import re
from datetime import datetime, date
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor as ThreadPool

# Fixed logo variable
logo = """   
logo = """
\033[1;35m███████╗ █████╗ ██████╗  █████╗ ███████╗
\033[1;36m██╔════╝██╔══██╗██╔══██╗██╔══██╗╚══███╔╝
\033[1;34m█████╗  ███████║██████╔╝███████║  ███╔╝ 
\033[1;32m██╔══╝  ██╔══██║██╔══██╗██╔══██║ ███╔╝  
\033[1;33m██║     ██║  ██║██║  ██║██║  ██║███████╗
\033[1;31m╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

\033[1;37m╭─────────────────────────────╮
│ \033[1;32m•͡˘㇁•͡˘ \033[1;35mF A R A Z \033[1;36m•͡˘㇁•͡˘ \033[1;37m│
╰─────────────────────────────╯

\033[1;33m┌─────────────────────────────┐
│ \033[1;34mCREATED BY \033[1;35m: FARAZ & TEAM \033[1;33m│
│ \033[1;34mGITHUB    \033[1;35m: FARAZ-DEV    \033[1;33m│
│ \033[1;34mVERSION   \033[1;35m: 3.0          \033[1;33m│
└─────────────────────────────┘

\033[1;36m✧･ﾟ: *✧･ﾟ:* \033[1;32mW \033[1;36m*:･ﾟ✧*:･ﾟ✧
       \33[37;41m\t WELLCOME TO Faraz TOOL\33[0;m
 
\033[1;37m================== \33[32;45mNIDA\33[0;m ======================\n"""

# Color definitions
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

def clear():
    os.system('clear')
    print(logo)

def ud():
    clear()
    print(logo)
    print(' [1] SUBSCRIBE MY CHANNEL')
    print(' [2] EXIT')
    opt = input('\n   Choose option >>> ')
    if opt == '1':
        os.system('xdg-open ')
        FD()
    else:
        print('\n\x1b[1;31mEXIT\x1b[0;97m')
        sys.exit()

def FD():
    clear()
    print(logo)
    print('\x1b[1;33m [1] SUBSCRIBE MY FRIEND CHANNEL')
    print(' [2] EXIT')
    opt = input('\n  \x1b[1;32m Choose option >>> ')
    if opt == '1':
        os.system('xdg-open https://youtu.be/y837qD_AO6Q')
        o()
    else:
        print('\n\x1b[1;31mEXIT\x1b[0;97m')
        sys.exit()

def o():
    clear()
    print(logo)
    print('\t🔥🔥RANDOM NUMBER CRACK🔥🔥')
    print('')
    print('\x1b[1;32m [1]\x1b[1;33m RANDOM CRACK ')
    print('\x1b[1;32m [2] \x1b[1;32mCONTACT ME ON FACEBOOK')
    print(' \x1b[1;32m[3] \x1b[1;32mSUBSCRIBE MY CHANNEL')
    print(' \x1b[1;32m[4] \x1b[1;32mJOIN FB GROUP')
    print(' \x1b[1;32m[00] \x1b[1;31mEXIT')
    opt = input('\n   \x1b[1;32m Choose option >>> ')
    if opt == '1':
        i()
    elif opt == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100082840689031')
    elif opt == '3':
        os.system('xdg-open https://youtube.com/channel/UCG8CSxk8KQMZuVfRhCa6FBw')
    elif opt == '4':
        os.system('xdg-open https://facebook.com/groups/207678473842318/')
    elif opt == '00':
        sys.exit()
    else:
        print('\n\x1b[1;31m Choose valid option\x1b[0;97m')

# [Rest of your functions like i(), rcrack(), etc. can be added here]

if __name__ == "__main__":
    try:
        ud()
    except KeyboardInterrupt:
        print("\n\x1b[1;31mProcess interrupted by user\x1b[0m")
    except Exception as e:
        print(f"\x1b[1;31mError occurred: {e}\x1b[0m")
    finally:
        print("\x1b[1;32mScript execution completed\x1b[0m")
