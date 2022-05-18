import requests
from sys import argv

message = "hello"
print(message)

with open("vuldb_api.txt", "r") as f:
    key = f.read()

print("hello")
product = argv[1]
version = argv[2]

print(product,version)

def VuldbLookup(product, version=None):
    url = "https://vuldb.com/?api"
    if version:
        q = "product:%s,version:%s" % (product,version)
    else:
        q = "product:%s" % product

    query = { 
        "apikey":key,
        "advancedsearch":q
    }

    results = requests.post(url,query)
    j = results.json()

    print(j)

    '''if "results" in j:
        sources = [result["source"] for result in j["result"] if "source in result"]
        return sources
    else:
        return []'''
