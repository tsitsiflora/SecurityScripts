# You have 100 computers that centrally log outbound netflow sockets to "netflow.txt".
# You want to alert yourself if any of your devices  start port scanning, as that could indicate compromise. 
# The central log file is of this format: "saddr:port -> daddr:port"
# 
# Write a script that prints out Source IPs that have connected to >=3 unique ports of a Dest IP
# 
# For example:
# 192.168.42.1:1337 -> 216.58.195.236:22
# 192.168.42.1:1234 -> 216.58.195.237:22
# 192.168.42.1:5555 -> 216.58.195.238:22
# Should have no output
# 
# 192.168.42.1:1234 -> 216.58.195.236:22
# 192.168.42.1:1337 -> 216.58.195.237:23
# 192.168.42.1:5555 -> 216.58.195.238:24
# Should have no output
# 
# 192.168.42.2:5555 -> 216.58.195.238:22
# 192.168.42.2:1337 -> 216.58.195.238:80
# 192.168.42.2:1234 -> 216.58.195.238:443
# 192.168.42.1:5555 -> 216.58.195.238:24
# Should output: 192.168.42.2