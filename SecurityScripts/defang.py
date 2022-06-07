# the script defangs an IP address

from ast import Str

# using loops
def defang(IP):
	ans = ""
	for chr in IP:
		if chr == ".":
			chr = "[.]" # replace the . in the IP with [.]
			ans += chr
		else:
			ans += chr
	return ans

result = defang("192.168.0.56")
print(result)

# using the built in function replace
def defang_IP(ip):
    for char in ip:
        char.replace(".", "[.]")

output = defang("172.160.34.10")
print(output)

# using split 
def defang_ip_address(ip_address):
    new_address = ""
    split_address = ip_address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address

ip_address = defang_ip_address("255.255.255.0")
print(ip_address)