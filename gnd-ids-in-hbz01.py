# This script runs a list of GND persons against lobid-resources API and creates a list of hbzIds of titles that link to those persons .
# Ticket for background: https://github.com/hbz/lobid/issues/417
# 1st step for generating the list:$ curl --header "Accept: application/x-jsonlines" "http://lobid.org/gnd/search?q=dateOfDeath%3A%5B*+TO+1949%5D" | jq -r .gndIdentifier > gndPersonsDeadBefore1949.txt

import requests
import json

filepath = 'gnd1949-test.txt'

fp = open(filepath)#
total = 0
titles = []

def build_url(gndId):
    return 'http://weywot4.hbz-nrw.de:9200/resources/_search?q=contribution.agent.id%3A%22https\:\/\/d-nb.info\/gnd\/' + gndId.rstrip('\n') + '%22'
#    return 'https://lobid.org/resources/search?q=contribution.agent.id%3A%22https\:\/\/d-nb.info\/gnd\/' + gndId.rstrip('\n') + '%22'

for gndId in fp.readlines():
    if requests.get(build_url(gndId)).json()['hits']['total'] > 0:
#    if requests.get(build_url(gndId)).json()['totalItems'] > 0:
        for title in requests.get(build_url(gndId)).json()['hits']['hits']:
#        for title in requests.get(build_url(gndId)).json()['member']:
            print(title['hbzId'])
            titles.append(title['hbzId'])

with open('moeglicherweise-gemeinfrei.txt', 'w') as f:
    for i in titles:
        f.write("%s\n" % i)