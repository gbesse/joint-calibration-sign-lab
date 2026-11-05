import unittest,math
from joint_calibration_sign_lab.core import run
class DomainTests(unittest.TestCase):
 def test_reverse_sign(self):
  x=run({'ticks_per_turn':4,'samples':[dict(raw_ticks=1,reference_radians=0),dict(raw_ticks=2,reference_radians=-math.pi/2)]});self.assertEqual(x['best']['sign'],-1);self.assertAlmostEqual(x['best']['offset_ticks'],1)
 def test_forward(self):self.assertEqual(run({'ticks_per_turn':4,'samples':[dict(raw_ticks=0,reference_radians=0),dict(raw_ticks=1,reference_radians=math.pi/2)]})['best']['sign'],1)
 def test_no_excitation(self):
  with self.assertRaises(ValueError):run({'ticks_per_turn':4,'samples':[dict(raw_ticks=1,reference_radians=0)]*2})
