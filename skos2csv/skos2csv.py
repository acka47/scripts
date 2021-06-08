import rdflib

g = rdflib.Graph()

# Load file in format ttl
g.parse("hochschulfaechersystematik.ttl", format="ttl")

# SPARQL query for URI and label of each concept
qres = g.query(
    """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?concept ?label
       WHERE {
           ?concept a skos:Concept ;
                skos:prefLabel ?label
       }""")

# Write results to file per line
with open("hochschulfaechersystematik.csv", "a") as output:
    for row in qres:
            output.write("%s ; %s" % row) #  separate ?concept and ?label with comma 
            output.write("\n") # add a new line delimiter to start new line
