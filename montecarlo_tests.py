import unittest
import enchant
import numpy as np
import pandas as pd
from montecarlo import *
from turtle import color
from sympy import GreaterThan
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None


class DieTestSuite(unittest.TestCase):

    def test_1_DIE_change_weight(self):
        dieObject.change_weight(6,5)
        faces = [1,2,3,4,5,6]
        weights = [1.0, 1.0, 1.0, 1.0, 1.0, 5.0]
        expected = pd.DataFrame({
            'faces': faces,
            'weights': weights
        })
        pd.testing.assert_frame_equal(dieObject.showCurrent(), expected)


    def test_2_DIE_rollDie(self):
        
        length = len(dieObject.rollDie(20))
        expected=20
        self.assertEqual(length, expected)


    def test_3_DIE_showCurrent_die(self):
        df = dieObject.showCurrent()
        self.assertEqual(list(df.shape),[6,2])



class GameTestSuite(unittest.TestCase):

    def test_4_GAME_play(self):
        gameObject.play(1000)
        self.assertEqual(list(gameObject._dfgame.shape),[1000,2])

    def test_5_GAME_show(self):
        self.assertEqual(list(gameObject.show().shape), [1000,2])




class AnalyzerTestSuite(unittest.TestCase):

    def test_6_ANALYZER_jackpot(self):
        gameObject.play(1000)
        analyzerObject = Analyzer(gameObject)
        self.assertGreater(analyzerObject.jackpot(),0)


    def test_7_ANALYZER_combo(self):
        gameObject.play(1000)
        analyzerObject = Analyzer(gameObject)
        analyzerObject.combo()
        self.assertEqual(analyzerObject.comboDF['frequencies'].sum(),1000)

    def test_8_ANALYZER_facecounts(self):
        gameObject.play(1000)
        analyzerObject = Analyzer(gameObject)
        analyzerObject.facecountsperroll()
        self.assertEqual(len(analyzerObject.facecountsDF), 1000)




if __name__ == '__main__':
    dieObject = Die([1,2,3,4,5,6])
    gameObject = Game([dieObject, dieObject])
    unittest.main(verbosity=3)