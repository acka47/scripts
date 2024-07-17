import rdflib
from rdflib import Graph

g = rdflib.Graph()

# Load file in format ttl
g.parse("rpb-spatial.ttl", format="ttl")

# SPARQL query for URI and label of each concept
qres = g.query(
    """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?label ?concept ?definition
       WHERE {
           ?concept a skos:Concept ;
                skos:prefLabel ?label ;
                skos:definition ?definition
       }""")

# Write results to file per line
with open("rpb-spatial.ndjson", "a") as output:
    for row in qres:
        output.write("{\"prefLabel\":\"%s\",\"uri\":\"%s\",\"definition\":\"%s\"}" % row) 
        output.write("\n") # add a new line delimiter to start new line
