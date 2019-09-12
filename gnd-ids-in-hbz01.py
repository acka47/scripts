# This script runs a list of GND IDs against lobid-resources API andcounts how many of the requests have one ore more hits.
# Ticket forbackground: https://github.com/hbz/lobid-gnd/issues/222
# 1st step for generating the list: $ curl --header "Accept: application/x-jsonlines" "http://lobid.org/gnd/search?q=type%3AUndifferentiatedPerson+AND+_exists_%3AvariantName&size=10" | jq -r .id > undifferentiated-with-variantName.txt

import requests
import json

filepath = 'undifferentiated-with-variantName.txt'

fp = open(filepath)#
total = 0
count = 0

def build_url(id):
    return 'http://weywot4.hbz-nrw.de:9200/resources-20190908-0100/_search?q=contribution.agent.id%3A%22' + id.rstrip() + '%22'

for id in fp.readlines():
    total += 1
    if requests.get(build_url(id)).json()['hits']['total'] > 0:
        count += 1
        print("%s IDs of %s are in hbz01." % (count, total))
