import requests
import json
import config

# schema


def create_schema():
    str_gremlin_dsl = """
	//open graph management
	mgmt = graph.openManagement();\
	//properties with common names across nodes, declared only once.
	if(null == mgmt.getPropertyKey('name')) {
		    name = mgmt.makePropertyKey('name').dataType(String.class).make();
		}
	if(null == mgmt.getPropertyKey('age')) {
		    age = mgmt.makePropertyKey('age').dataType(String.class).make();
		}
            if(null == mgmt.getPropertyKey('loves_to_read')) {
                            loves_to_read = mgmt.makePropertyKey('loves_to_read').dataType(Boolean.class).make();
                        }
	//edge lables
	if(null == mgmt.getEdgeLabel('founder_of')) {
		    founder_of= mgmt.makeEdgeLabel('founder_of').make();
		}
	if(null == mgmt.getEdgeLabel('bod_at')) {
		    bod_at = mgmt.makeEdgeLabel('bod_at').make();
		}
	if(null == mgmt.getEdgeLabel('works_at')) {
		     works_at = mgmt.makeEdgeLabel('works_at').make();
		}
            if(null == mgmt.getEdgeLabel('director_of')) {
                            director_of = mgmt.makeEdgeLabel('director_of').make();
                        }
            if(null == mgmt.getEdgeLabel('knows')) {
                            knows = mgmt.makeEdgeLabel('knows').make();
                        }

	//vertex labels
	if(null == mgmt.getVertexLabel('Person')) {
		     Person = mgmt.makeEdgeLabel('Person').make();
		}
	if(null == mgmt.getVertexLabel('Org')) {
		     Organization = mgmt.makeEdgeLabel('Organization').make();
		}
	if(null == mgmt.getEdgeLabel('City')) {
		     Group = mgmt.makeEdgeLabel('City').make();
		}

            // set an index on property name, along with uniqueness constraint
            iif(null == mgmt.getGraphIndex('NameIndex')) {
            mgmt.buildIndex('NameIndex', Vertex.class).addKey(name).unique().buildCompositeIndex();
                        }
	mgmt.commit();
	"""
    return str_gremlin_dsl


def execute_gremlin_dsl(str_gremlin_dsl):
    url = config.GREMLIN_SERVER_URL_REST
    payload = {'gremlin': str_gremlin_dsl}
    response = requests.post(url, data=json.dumps(payload))
    response
    json_response = response.json()
    print(json_response)


str_gremlin_dsl = create_schema()
execute_gremlin_dsl(str_gremlin_dsl)
