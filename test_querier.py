#from __future__ import absolute_import
import unittest
from querier import Querier
import requests
import sys

"""
Test the connection to and number of entries from Materials Project.
1st argument user's API_KEY
"""

class QuerierTestCase(unittest.TestCase):
    """Tests for `querier.py`."""

    def test_connect(self):
        """
        Check the connection with the MP api_check
        """
        response = requests.get('https://www.materialsproject.org/rest/v1/api_check',
                                {'API_KEY': API_KEY})
        self.assertTrue(response.ok)

    def test_querier(self):
        """
        If the number of entries for Fe2O3 in the MP is larger or equal to 12.
        The larger case is for in case more have been added in the future.
        """
        self.assertTrue(len(Querier(API_KEY, 'Fe2O3').mp_all) >= 12,
                        msg='Number of entries for Fe2O3 is not correct')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit("Your API_KEY must be supplied as an argument to these tests !")
    API_KEY = sys.argv[1]
    del sys.argv[1:]
    unittest.main()
