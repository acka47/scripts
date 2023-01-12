# This script runs a list of ZDB IDs against lobid-resources API 
# and gives back the corresponding hbz ID.

import requests
import json

filepath = 'zdbIDs.txt'

fp = open(filepath)

def build_url(id):
    return 'https://lobid.org/resources/search?q=zdbId:' + id.rstrip()

for zdbId in fp.readlines():
    hbzId = requests.get(build_url(zdbId)).json()['member'][0]['hbzId']
    print(zdbId.rstrip(), hbzId, sep='\t')
