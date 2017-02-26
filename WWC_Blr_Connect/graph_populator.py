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


def get_dict(value_list):
    value_dict = {key: None for key in value_list}
    return value_dict


def add_vertex(label, key):
    return g.addV(label).property('name', key).toList()


def add_edges(id1, id2, label):
    print g.V(id1).addE(label).to(g.V(id2)).toList()


def populate_vertex(value_dict, label):
    for key in value_dict:
        result = add_vertex(label, key)
        value_dict[key] = result[0].id
        print value_dict[key]
    return value_dict


def add_person_knows(names_dict):
    n = names_dict
    add_edges(n['Saif'], n['Zishan'], 'knows')
    add_edges(n['Saif'], n['Umar'], 'knows')
    add_edges(n['Saif'], n['Sarah'], 'knows')
    add_edges(n['Umar'], n['Sarah'], 'knows')
    add_edges(n['Neha'], n['Zishan'], 'knows')


def add_person_comapany(names_dict, org_dict):
    n = names_dict
    o = org_dict
    add_edges(n['Saif'], o['Redhat'], 'works_at')
    add_edges(n['Zishan'], o['Redhat'], 'works_at')
    add_edges(n['Umar'], o['Google'], 'works_at')
    add_edges(n['Sarah'], o['Accenture'], 'works_at')


def add_person_group(names_dict, group_dict):
    n = names_dict
    m = group_dict
    add_edges(n['Saif'], m['AI'], 'member_of')
    add_edges(n['Saif'], m['FunMaths'], 'member_of')
    add_edges(n['Umar'], m['AI'], 'member_of')
    add_edges(n['Neha'], m['FunMaths'], 'member_of')


org_list = ['Redhat', 'Google', 'Accenture']
group_list = ['AI', 'FunMaths']
names_list = ['Saif', 'Zishan', 'Umar', 'Neha', 'Sarah']
org_dict = get_dict(org_list)
group_dict = get_dict(group_list)
names_dict = get_dict(names_list)

org_dict = populate_vertex(org_dict, label='Organization')
group_dict = populate_vertex(group_dict, label='Group')
names_dict = populate_vertex(names_dict, label='Person')

add_person_comapany(names_dict, org_dict)
add_person_knows(names_dict)
add_person_group(names_dict, group_dict)
