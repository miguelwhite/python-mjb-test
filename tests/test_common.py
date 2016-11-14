import sys
import os
import unittest

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),'../'))
from mjb_test import common

class Test(unittest.TestCase):
  def test_responses(self):
    self.assertTrue(common.prompt_and_confirm(response='y'))
    self.assertTrue(common.prompt_and_confirm(response='Y'))
    self.assertFalse(common.prompt_and_confirm(response='n'))
    self.assertFalse(common.prompt_and_confirm(response='N'))
    with self.assertRaises(SystemExit):
      common.prompt_and_confirm(response='n', exit_on_false=True)
