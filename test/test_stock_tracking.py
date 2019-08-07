import pytest
from stock_track_app.app import show_default, edit_default, get_prices, add_list
import pandas_datareader as pdr

class TestClass:
    def test_showdefault(self):
        symbols = "AMZN GOOG NFLX FB GLD SPY".split()
        result = show_default(symbols)
        assert len(result) == 6
        assert 'AMZN' in result
        assert 'SPY' in result
