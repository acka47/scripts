# This script runs a list of GND persons against lobid-resources API and creates a list of hbzIds of titles that link to those persons .
# Ticket for background: https://github.com/hbz/lobid/issues/417
# 1st step for generating the list:$ curl --header "Accept: application/x-jsonlines" "http://lobid.org/gnd/search?q=dateOfDeath%3A%5B*+TO+1949%5D" | jq -r .gndIdentifier > gndPersonsDeadBefore1949.txt

import requests
import json

filepath = 'input.txt'

fp = open(filepath)#
total = 0
titles = []

def build_url(gndId):
    return 'http://weywot4.hbz-nrw.de:9200/resources/_search?q=contribution.agent.id%3A%22https\:\/\/d-nb.info\/gnd\/' + gndId.rstrip('\n') + '%22&size=250'

for gndId in fp.readlines():
    if requests.get(build_url(gndId)).json()['hits']['total'] > 0:
        for title in requests.get(build_url(gndId)).json()['hits']['hits']:
            print(title['_id'])
            titles.append(title['_id'])

with open('output.txt', 'w') as f:
    for i in titles:
        f.write("%s\n" % i)