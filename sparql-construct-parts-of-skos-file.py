import rdflib

g = rdflib.Graph()

g.parse("nwbib-spatial.ttl", format="ttl")

qres = g.query(
    """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

    CONSTRUCT { ?x skos:broader <https://nwbib.de/spatial#N74> }
       WHERE {
           { ?x skos:broader <https://nwbib.de/spatial#N74> }
       }""")

with open("74.nt", "w") as output:
            output.write(qres.serialize(format='nt'))