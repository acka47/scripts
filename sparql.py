import rdflib

g = rdflib.Graph()

g.parse("filename.ttl", format="ttl")

qres = g.query(
    """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    SELECT ?x ?y
       WHERE {

       }""")

for row in qres:
    print("%s has relation to %s" % row)
