from flowmapper.utils import read_field_mapping, read_flowlist, read_migration_files
from flowmapper.flowmap import Flowmap
from flowmapper.flow import Flow

def test_flowmap(snapshot_json):
    
    field_mapping = 'config/simapro-ecoinvent.py'
    source_flows_path = 'data/industry-2.0-biosphere.json'
    target_flows_path = 'data/ecoinvent-3.9-biosphere.json'
    
    fields = read_field_mapping(field_mapping)
    transformations = read_migration_files('config/sp-formatted.json')
    
    source_flows = read_flowlist(source_flows_path)
    source_flows = [Flow(flow, fields['source'], transformations) for flow in source_flows]
    target_flows = read_flowlist(target_flows_path)
    target_flows = [Flow(flow, fields['target']) for flow in target_flows]

    flowmap = Flowmap(source_flows, target_flows)
    actual = flowmap.to_randonneur()
    assert actual == snapshot_json
