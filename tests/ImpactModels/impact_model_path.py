import unittest
import os

from src.py2graphdb.config import config as CONFIG
from impact_model_ks import *

node_ids = {
    "Organization": "org_001",
    "ImpactModel": "impact_model_001",
    "Program": "prog_001",
    "Service": "service_001",
    "Activity": "activity_001",
    "Input": "input_001",
    "Output": "output_001",
    "Outcome": "outcome_001",
    "Stakeholder": "stakeholder_001",
    "StakeholderOutcome": "stakeholder_outcome_001",
    "ImpactReport": "impact_report_001",
    "ImpactRisk": "impact_risk_001",
    "Indicator": "indicator_001",
    "IndicatorReport": "indicator_report_001",
    "ImpactScale": "impact_scale_001",
    "ImpactDepth": "impact_depth_001",
    "ImpactDuration": "impact_duration_001"
}

if os.path.exists(CONFIG.LOG_FILE):
    os.remove(CONFIG.LOG_FILE)

from owlready2 import default_world, onto_path

onto_path.append('input/ontology_cache/')

im = default_world.get_ontology(CONFIG.NM)
from src.py2graphdb.ontology.operators import *

CONFIG.STORE_LOCAL = False
with im:
    from src.py2graphdb.utils.db_utils import SPARQLDict
    from impact_model_ks import ImpactModelNode
    print()

def create_node(node_class, id):
    return node_class(inst_id=f'im.{node_ids[id]}', keep_db_in_synch=True)


def delete_node(node_class, id):
    node_class(inst_id=f'im.{node_ids[id]}', keep_db_in_synch=True).delete()


def init_test_node(node_class, id):
    delete_node(node_class, id)
    return create_node(node_class, id)


class ImpactModelConfig():
    def __init__(self):
        self.init_config()

    nodes = []

    def init_config(self):
        with im:
            org = init_test_node(OrganizationNode, "Organization")
            impact_model = init_test_node(ImpactModelNode, "ImpactModel")
            program = init_test_node(ProgramNode, "Program")
            service = init_test_node(ServiceNode, "Service")
            activity = init_test_node(ActivityNode, "Activity")
            input = init_test_node(InputNode, "Input")
            output = init_test_node(OutputNode, "Output")
            outcome = init_test_node(OutcomeNode, "Outcome")
            stakeholder = init_test_node(StakeholderNode, "Stakeholder")
            stakeholder_outcome = init_test_node(StakeholderOutcomeNode, "StakeholderOutcome")
            impact_report = init_test_node(ImpactReportNode, "ImpactReport")
            impact_risk = init_test_node(ImpactRiskNode, "ImpactRisk")
            indicator = init_test_node(IndicatorNode, "Indicator")
            indicator_report = init_test_node(IndicatorReportNode, "IndicatorReport")
            impact_scale = init_test_node(ImpactScaleNode, "ImpactScale")
            impact_depth = init_test_node(ImpactDepthNode, "ImpactDepth")
            impact_duration = init_test_node(ImpactDurationNode, "ImpactDuration")
            

            input.has_contributing_stakeholder = stakeholder.inst_id

            impact_model.has_stakeholder = stakeholder.inst_id
            impact_model.has_program = program.inst_id
            impact_model.for_organization = org.inst_id
            
            program.has_service = service.inst_id

            service.has_elaboration = activity.inst_id
            service.has_outcome = outcome.inst_id

            activity.has_input = input.inst_id
            activity.has_output = output.inst_id
            activity.can_produce = outcome.inst_id

            outcome.can_enable = activity.inst_id
            outcome.has_impact_risk = impact_risk.inst_id
            outcome.has_indicator = indicator.inst_id
            outcome.has_stakeholder_outcome = stakeholder_outcome.inst_id

            stakeholder_outcome.for_stakeholder = stakeholder.inst_id
            stakeholder_outcome.has_impact_report = impact_report.inst_id

            indicator.uses_output = output.inst_id
            indicator.has_indicator_report = indicator_report.inst_id

            impact_report.has_scale = impact_scale.inst_id
            impact_report.has_depth = impact_depth.inst_id
            impact_report.has_duration = impact_duration.inst_id

            self.nodes = [
                org, impact_model, program, service, activity, input, output, outcome, stakeholder,
                stakeholder_outcome, impact_report, impact_risk, indicator, indicator_report,
                impact_scale, impact_depth, impact_duration
            ]
class TestImpactModelPathConfig(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # save classes and methods in graph
        from graphdb_importer import import_and_wait, set_config
        TMP_DIR = './tmp/'
        _ = os.makedirs(TMP_DIR) if not os.path.exists(TMP_DIR) else None
        owl_file = f'{TMP_DIR}impact_model_path.owl'
        im.save(owl_file)
        set_config(CONFIG.SERVER_URL, CONFIG.REPOSITORY, username='admin', password='admin')
        import_and_wait(owl_file, replace_graph=True)

        SPARQLDict._clear_graph(graph=CONFIG.GRAPH_NAME)

        _ = ImpactModelConfig()

    def test_path_1(self):
        with im:
            start = 'im.ImpactModel'
            end = 'im.ImpactReport'
            res = SPARQLDict._process_path_request(start, end, action='collect', direction='children', how='shortest')
            expected_output = [{'start': 'im.ImpactModel', 'end': 'im.ImpactReport', 'path': ['im.Program', 'im.Service', 'im.Outcome', 'im.StakeholderOutcome']}]
            self.assertEqual(res, expected_output)

    def test_path_2(self):
        with im:
            start = 'im.ImpactModel'
            end = 'im.ImpactReport'
            res = SPARQLDict._process_path_request(start, end, action='collect', direction='children', how='all')
            expected_output = [{'start': 'im.ImpactModel', 'end': 'im.ImpactReport', 'path': ['im.Program', 'im.Service', 'im.Activity', 'im.Outcome', 'im.StakeholderOutcome']},
                                {'start': 'im.ImpactModel', 'end': 'im.ImpactReport', 'path': ['im.Program', 'im.Service', 'im.Outcome', 'im.StakeholderOutcome']}]
            self.assertEqual(res, expected_output)

    def test_path_3(self):
        with im:
            start = 'im.ImpactModel'
            end = 'im.ImpactReport'
            res = SPARQLDict._process_path_request(start, end, action='collect', direction='children', how='first')
            expected_output = {'start': 'im.ImpactModel', 'end': 'im.ImpactReport', 'path': ['im.Program', 'im.Service', 'im.Outcome', 'im.StakeholderOutcome']}
            self.assertEqual(res, expected_output)
            
if __name__ == '__main__':
    unittest.main(exit=False)
