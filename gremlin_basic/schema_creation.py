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
	if(null == mgmt.getPropertyKey('skills')) {
		    skills = mgmt.makePropertyKey('skills').dataType(String.class).make();
		}
	//edge lables
	if(null == mgmt.getEdgeLabel('works_at')) {
		    works_at = mgmt.makeEdgeLabel('works_at').make();
		}
	if(null == mgmt.getEdgeLabel('knows')) {
		    knows = mgmt.makeEdgeLabel('knows').make();
		}
	if(null == mgmt.getEdgeLabel('works_at')) {
		     member_of = mgmt.makeEdgeLabel('member_of').make();
		}

	//vertex labels
	if(null == mgmt.getVertexLabel('Person')) {
		     Person = mgmt.makeEdgeLabel('Person').make();
		}
	if(null == mgmt.getVertexLabel('Organization')) {
		     Organization = mgmt.makeEdgeLabel('Organization').make();
		}
	if(null == mgmt.getEdgeLabel('Group')) {
		     Group = mgmt.makeEdgeLabel('Group').make();
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
