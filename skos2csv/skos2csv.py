import rdflib

g = rdflib.Graph()

g.parse("hochschulfaechersystematik.ttl", format="ttl")

qres = g.query(
    """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?concept ?label
       WHERE {
           ?concept a skos:Concept ;
                skos:prefLabel ?label
       }""")

with open("hochschulfaechersystematik.csv", "a") as output:
    for row in qres:
            output.write("%s ; %s" % row)
            output.write("\n")
