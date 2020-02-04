import requests
import json

filepath = '/home/acka47/git/scripts/202002-undifferentiated-with-variantName.ndjson'
input = open(filepath).readlines()

def build_url(id):
    # return 'https://lobid.org/resources/search?q=contribution.agent.id%3A' + id.rstrip() + '&format=json'
    return 'http://weywot4.hbz-nrw.de:9200/resources/_search?q=_exists_%3AhasItem+AND+contribution.agent.id%3A"' + id.rstrip() + '"&format=json'


for row in input:
     data = json.loads(row.rstrip())
     id = data['id']
     r = requests.get(build_url(id))
     if r.json()['hits']['total'] > 0:
         titles = []
         for entry in r.json()['hits']['hits']:
             title = {}
             hbzId = entry['_source']['hbzId']
             title.update({"hbzId": hbzId})
             owners = []
             for item in entry['_source']['hasItem']:
                 if 'heldBy' in item:
                     owner = item['heldBy']['id']
                     owners.append(owner)
             title.update({"owners": owners})
             titles.append(title)
         data.update({"hasTitle": titles} )
