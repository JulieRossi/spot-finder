from elasticsearch_dsl import DocType, Text
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['localhost'])


class Spot(DocType):
    site = Text()
    spot_name = Text()
    routes = Text()

    class Meta:
        index = 'spots'
