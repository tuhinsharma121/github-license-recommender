import logging

from src.github_license_graph import GithubLicenseGraph

logging.basicConfig(filename="/tmp/error.txt", level=logging.DEBUG)
logger = logging.getLogger(__name__)

from unittest import TestCase


class TestGithubLicenseGraph(TestCase):
    def test_license_recommendation_for_license_list(self):
        g = GithubLicenseGraph.train()
        self.assertTrue(g != None)
        g.save(filename="test/data/github_license_graph.pkl")
        g = GithubLicenseGraph.load(filename="test/data/github_license_graph.pkl")
        m = g.get_license_recommendation_for_license_list(['LGPL V2.1', 'APACHE'])
        self.assertTrue((m == "gpl3"))
        m = g.get_license_recommendation_for_license_list(['PD', 'APACHE'])
        self.assertTrue((m == "apache"))
        m = g.get_license_recommendation_for_license_list(['BSD', 'LGPL V2.1+'])
        self.assertTrue((m == "lgpl22"))
        m = g.get_license_recommendation_for_license_list(['BSD', 'LGPL V2.1+', 'GPL V3+'])
        self.assertTrue((m == "gpl3"))
        m = g.get_license_recommendation_for_license_list(['MIT', 'GPL V2+', 'APACHE'])
        self.assertTrue((m == "gpl3"))
        m = g.get_license_recommendation_for_license_list(['GPL V2', 'APACHE'])
        self.assertTrue((m == None))
