import os
import sys
import subprocess as sp

import unittest
import logging

maindir = os.getcwd()  # ../scr folder
src_dir = os.path.join(maindir, 'src', 'stock_track_app')
# /Users/manuelrodriguez/dev/PYTHON/stocks_tracking/scr/stock_track_app
# /Users/manuelrodriguez/dev/PYTHON/stocks_tracking/src/stock_track_app
print(src_dir)
sys.path.insert(0, src_dir)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('[%(levelname)-2s] %(message)s')
handler.setFormatter(formatter)


if __name__ == '__main__':


    pattern = sys.argv[1] if len(sys.argv) >=2 else "test*.py"
    if pattern == 'all':
        pattern = "test*.py"
    test_dir = sys.argv[2] if len(sys.argv) >=3 else "test"

    sys.path.insert(0, test_dir)
    print("Running {} within {}".format(pattern, test_dir))

    #sp.run(['python', '-m', 'unittest', "discover", "test"], )
    test_loader = unittest.defaultTestLoader.discover(test_dir, pattern)
    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_loader)

    #
    sys.exit(not result.wasSuccessful())
