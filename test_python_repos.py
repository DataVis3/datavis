import unittest

from python_repos import *


class TestPythonRepos(unittest.TestCase):
    def test_success(self):
        self.assertEqual(r.status_code, 200)

    def test_repo_min(self):
        self.assertGreater(response_dict['total_count'], 1000)

    def test_repo_return(self):
        self.assertEqual(len(repo_dicts), 30)
