# coding: utf8
# 1st step: $ curl --header "Accept: application/x-jsonlines" "http://lobid.org/resources/search?q=spatial.id%3A%22https%3A%2F%2Fnwbib.de%2Fspatial%23N74%22" > 74.ndjson

import logging
import rdflib

logging.basicConfig()
filepath = '74-2.ndjson'
input = open(filepath).readlines()
g=rdflib.Graph()

for line in input:
    g.parse(data=line, format="json-ld")

g.parse("74.nt", format="nt")

qres = g.query(
    """SELECT DISTINCT ?resource
       WHERE {
           ?resource <http://purl.org/dc/terms/spatial> [ 
               <http://www.w3.org/2004/02/skos/core#broader> <https://nwbib.de/spatial#N74>
               ] .
       }""")


with open("result2.txt", "a") as output:
    for row in qres:
            output.write("%s" % row)
            output.write("\n")
