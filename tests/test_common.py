import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))
from mjb_test import common

class Test(unittest.TestCase):
  def test_responses(self):
    self.assertEqual(common.foo(), 'Hello World!')
