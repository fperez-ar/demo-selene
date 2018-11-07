import unittest
from store_test import store_test

def suite():
    suite_test = unittest.TestSuite()
    # further tests WILL need to be added manually
    #TODO: parse and load all files from test directory
    suite_test.addTest(store_test('test_email'))
    return suite_test

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
