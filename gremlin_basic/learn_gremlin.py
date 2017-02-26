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


print('\n----Lets get the first connection people of Saif')
l1 = g.V().has('name', 'Saif').out('knows').values('name').toList()
print(l1)

print('\n----Now lets get the second level connection peoplr of Saif')
l2 = g.V().has('name', 'Saif').out('knows').out('knows').values('name').toList()
for i in l2:
    if i not in l1:
        print(i)

print('\n----Lets find the people who are currently not working anywhere')
result = g.V().hasLabel('Person').not_(outE('works_at')).values('name').toList()
print(result)

id1 = g.V().has('name', 'Umar').toList()[0]
id2 = g.V().has('name', 'Accenture').toList()[0]
g.V(id1.id).addE('works_at').to(g.V(id2.id)).toList()

print('\n--- All the peopel who are working')
result = g.V().hasLabel('Organization').in_('works_at').values('name').toList()
print(result)
print('Number of working people, with repetition= %d', len(result))

print('\n----Lets remove the duplicate name from the list, and print the total number of people who are working')
result = g.V().hasLabel('Organization').in_('works_at').dedup().count().toList()
print(result)
