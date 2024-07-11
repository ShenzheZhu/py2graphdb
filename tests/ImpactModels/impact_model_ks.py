from __main__ import *
from src.py2graphdb.Models.graph_node import GraphNode
from src.py2graphdb.utils.db_utils import PropertyList, SPARQLDict, Thing
from owlready2 import default_world, ObjectProperty, DataProperty, rdfs, Thing 
from src.py2graphdb.ontology.operators import *
from src.py2graphdb.config import config as CONFIG
im = default_world.get_ontology(CONFIG.NM)
from src.py2graphdb.utils.db_utils import PropertyList, SPARQLDict, resolve_nm_for_dict, Thing, _resolve_nm

with im:
    class hasContributingStakeholder(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates a contributing stakeholder"]

    class forOrganization(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the organization for which the impact model is created"]

    class hasStakeholder(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the stakeholder associated with the impact model"]

    class forStakeholder(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the stakeholder for which the outcome is measured"]

    class hasProgram(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the program associated with the impact model"]

    class hasService(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the service associated with the program"]

    class hasElaboration(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the elaboration activities associated with the service"]

    class hasInput(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the input associated with the activity"]

    class hasOutput(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the output associated with the activity"]

    class hasOutcome(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the outcome associated with the service"]

    class canProduce(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates that the outcome can produce a certain output"]

    class canEnable(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates that the outcome can enable a certain activity"]

    class hasStakeholderOutcome(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the stakeholder outcome associated with the impact model"]

    class hasImpactReport(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the impact report associated with the stakeholder outcome"]

    class hasImpactRisk(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the impact risk associated with the outcome"]

    class hasIndicator(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the indicator associated with the outcome"]

    class usesOutput(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates that the indicator uses a certain output"]

    class hasIndicatorReport(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the indicator report associated with the indicator"]

    class hasScale(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the scale associated with the impact report"]

    class hasDepth(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the depth associated with the impact report"]

    class hasDuration(ObjectProperty):
        range = [Thing]
        rdfs.comment = ["Indicates the duration associated with the impact report"]

class OrganizationNode(GraphNode):

    klass = 'im.OrganizationNode'
    relations = {}
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class ImpactModelNode(GraphNode):

    klass = 'im.ImpactModelNode'
    relations = {
        'for_organization': {'pred': im.forOrganization, 'cardinality': 'many'},
        'has_stakeholder': {'pred': im.hasStakeholder, 'cardinality': 'many'},
        'has_program': {'pred': im.hasProgram, 'cardinality': 'many'},
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class ProgramNode(GraphNode):

    klass = 'im.ProgramNode'
    relations = {
        'has_service': {'pred': im.hasService, 'cardinality': 'many'},
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class ServiceNode(GraphNode):

    klass = 'im.ServiceNode'
    relations = {
        'has_elaboration': {'pred': im.hasElaboration, 'cardinality': 'many'},
        'has_outcome': {'pred': im.hasOutcome, 'cardinality': 'many'},
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class ActivityNode(GraphNode):

    klass = 'im.ActivityNode'
    relations = {
        'has_input': {'pred': im.hasInput, 'cardinality': 'many'},
        'has_output': {'pred': im.hasOutput, 'cardinality': 'many'},
        'can_produce': {'pred': im.canProduce, 'cardinality': 'many'},
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class InputNode(GraphNode):

    klass = 'im.InputNode'
    relations = {
        'has_contributing_stakeholder': {'pred': im.hasContributingStakeholder, 'cardinality': 'many'},
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class OutputNode(GraphNode):

    klass = 'im.OutputNode'
    relations = {
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class OutcomeNode(GraphNode):

    klass = 'im.OutcomeNode'
    relations = {
        'can_enable': {'pred': im.canEnable, 'cardinality': 'many'},
        'has_impact_risk': {'pred': im.hasImpactRisk, 'cardinality': 'many'},
        'has_indicator': {'pred': im.hasIndicator, 'cardinality': 'many'},
        'has_stakeholder_outcome': {'pred': im.hasStakeholderOutcome, 'cardinality': 'many'},
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class StakeholderNode(GraphNode):

    klass = 'im.StakeholderNode'
    relations = {
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class StakeholderOutcomeNode(GraphNode):

    klass = 'im.StakeholderOutcomeNode'
    relations = {
        'for_stakeholder': {'pred': im.forStakeholder, 'cardinality': 'many'},
        'has_impact_report': {'pred': im.hasImpactReport, 'cardinality': 'many'},
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class ImpactReportNode(GraphNode):

    klass = 'im.ImpactReportNode'
    relations = {
        'has_scale': {'pred': im.hasScale, 'cardinality': 'many'},
        'has_depth': {'pred': im.hasDepth, 'cardinality': 'many'},
        'has_duration': {'pred': im.hasDuration, 'cardinality': 'many'},
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class ImpactRiskNode(GraphNode):

    klass = 'im.ImpactRiskNode'
    relations = {
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class IndicatorNode(GraphNode):

    klass = 'im.IndicatorNode'
    relations = {
        'uses_output': {'pred': im.usesOutput, 'cardinality': 'many'},
        'has_indicator_report': {'pred': im.hasIndicatorReport, 'cardinality': 'many'},
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class IndicatorReportNode(GraphNode):

    klass = 'im.IndicatorReportNode'
    relations = {
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class ImpactScaleNode(GraphNode):

    klass = 'im.ImpactScaleNode'
    relations = {
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class ImpactDepthNode(GraphNode):

    klass = 'im.ImpactDepthNode'
    relations = {
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)


class ImpactDurationNode(GraphNode):

    klass = 'im.ImpactDurationNode'
    relations = {
    }
    
    def __init__(self, inst_id=None, inst=None, keep_db_in_synch=False):
        super().__init__(inst_id=inst_id, inst=inst, keep_db_in_synch=keep_db_in_synch)

    imported_code = open('./src/py2graphdb/utils/_model_getters_setters_deleters.py').read()
    exec(imported_code)

