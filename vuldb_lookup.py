import requests
import sys

with open("vuldb_api.txt", "r") as f:
    key = f.read()

product = sys.argv[1]
version = sys.argv[2]

print(sys.argv[0])
print("Hello")