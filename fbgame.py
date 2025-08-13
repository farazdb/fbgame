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
\033[1;32m       888    d8P  8888888b.   .d8888b.  
\033[1;35m       888   d8P   888   Y88b d88P  Y88b 
\033[1;35m       888  d8P    888    888 Y88b.      
\033[1;32m       888d88K     888   d88P  "Y888b.   
\033[1;32m       8888888b    8888888P"      "Y88b. 
\033[1;35m       888  Y88b   888 T88b         "888 
\033[1;35m       888   Y88b  888  T88b  Y88b  d88P 
\033[1;32m       888    Y88b 888   T88b  "Y8888P"  
 
\033[1;37m================= \33[32;45mKASHIF\33[0;m =====================
\033[1;32m     \033[1;33mCREATED BY\33[0;m   :  \033[1;33mARYAN\33[0;m\033[1;32m && \033[1;33mKASHIF\33[0;m
\033[1;32m     \033[1;32mFACEBOK      : \033[1;34m ArYan KhAn
\033[1;32m     \033[1;35mGITHUB       :  \033[1;35mTEAM-KRS
\033[1;32m     \033[1;36mTOOL STATUS  :  \033[1;36mTOOL IS FREE
\033[1;32m     \033[1;35mTEAM         :  \033[1;35mKRS
\033[1;32m     \033[1;36mTOOL VIRSION :  \033[1;36m2.3
\033[1;37m================= \33[32;45mARYAN\33[0;m =====================
 
       \33[37;41m\t WELLCOME TO KRS TOOL\33[0;m
 
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
        os.system('xdg-open https://youtube.com/channel/UCG8CSxk8KQMZuVfRhCa6FBw')
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
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()
