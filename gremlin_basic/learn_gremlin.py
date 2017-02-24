import config
from gremlin_python import statics
from gremlin_python.structure.graph import Graph
from gremlin_python.process.graph_traversal import *
from gremlin_python.process.strategies import *
from gremlin_python.process.traversal import *
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection

graph = Graph()
g = graph.traversal().withRemote(DriverRemoteConnection(
    config.GREMLIN_SERVER_URL_WEBSOCKET, 'g'))


l1 = g.V().has('name', 'Saif').out('knows').values('name').toList()
print(l1)
l2 = g.V().has('name', 'Saif').out('knows').out('knows').values('name').toList()
print(l2)

result = g.V().has('name', 'Saif').as_('S').out('knows').as_('1st_level').out('knows').where(neq('1st_level'))by('name').toList()
print(result)
result = g.V().has('name', 'Saif').as_('S').out('knows').as_('1st_level').out(
    'knows').where(neq('1st_level')).by('name').toList()
print(result)
result = g.V().hasLabel('Person').not_(outE('works_at')).toList()
print(result)
result = g.V().hasLabel('Organization').in_('works_at').dedup().count().toList()
print(result)
result = g.V().hasLabel('Person').outE('works_at').count().toList()
print(result)
