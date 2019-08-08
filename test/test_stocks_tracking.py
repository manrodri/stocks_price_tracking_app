# import pytest
# from stock_track_app.app import show_default, edit_default, get_prices, add_list
# import pandas_datareader as pdr
#
# class TestClass:
import sys
import unittest
from app import show_default, edit_default, get_prices, add_list

class TestStrockTrackingApp(unittest.TestCase):
    def test_showdefault(self):
        symbols = "AMZN GOOG NFLX FB GLD SPY".split()
        result = show_default(symbols)
        self.assertEqual(len(result), 6)
        self.assertIn("AMZN", result)
        self.assertIn("SPY", result)


