import unittest
import enchant
import numpy as np
import pandas as pd
from MonteCarloSimulator.montecarlo import *
from turtle import color
from sympy import GreaterThan
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None


class DieTestSuite(unittest.TestCase):

    def test_1_DIE_change_weight(self):

        '''
        The die object of 6 faces has been created below. The weight for face 6 has been changed from 1.0 to 5.0
        This method checks to see that the change_weight method has run correctly, and the dataframe is updated with the new weight.
        Returns "ok" if the method returns a dataframe with the correct weights.
        '''

        dieObject.change_weight(6,5)
        faces = [1,2,3,4,5,6]
        weights = [1.0, 1.0, 1.0, 1.0, 1.0, 5.0]
        expected = pd.DataFrame({
            'faces': faces,
            'weights': weights
        })
        pd.testing.assert_frame_equal(dieObject.showCurrent(), expected)


    def test_2_DIE_rollDie(self):

        '''
        The die object of 6 faces has been created below. The die has been rolled 20 times.
        This test checks that the rollDie method has run correctly, by checking the length of the list of faces.
        Returns "ok" if the object has the correct length (20).
        '''
        
        length = len(dieObject.rollDie(20))
        expected=20
        self.assertEqual(length, expected)


    def test_3_DIE_showCurrent_die(self):

        '''
        The die object of 6 faces has been created below. 
        This test checks that the showCurrent method has run correctly, by checking the dimensions of the dataframe,
         which should have each row representing each face, and the column represents the weight for each face.
        Returns "ok" if the dataframe has the correct dimensions (6x2).
        '''

        df = dieObject.showCurrent()
        self.assertEqual(list(df.shape),[6,2])



class GameTestSuite(unittest.TestCase):

    def test_4_GAME_play(self):

        '''
        The game object has been created below containing two 6 sided die with all weights of 1.0
        This test checks that the play method has run correctly, by checking the dimensions of the dataframe,
         which should have the number of rows equal to the number of rolls, and the number of columns equal to the number of die.
        Returns "ok" if the dataframe has dimensions the correct dimensions (1000x2).
        '''

        gameObject.play(1000)
        self.assertEqual(list(gameObject._dfgame.shape),[1000,2])

    def test_5_GAME_show(self):

        '''
        The game object has been created below containing two 6 sided die with all weights of 1.0
        This test checks that the show method has run correctly, by checking the dimensions of the dataframe,
         which should have the number of rows equal to the number of rolls, and the number of columns equal to the number of die.
        Returns "ok" if the dataframe has the correct dimensions (1000x2).
        '''

        self.assertEqual(list(gameObject.show().shape), [1000,2])




class AnalyzerTestSuite(unittest.TestCase):

    def test_6_ANALYZER_jackpot(self):

        '''
        The analyzer object has been created by inputting the game object as the input parameter.
        This test checks that the jackpot method has run correctly, by counting the number of jackpots generated in 1000 rolls.
        Returns "ok" if the number of jackpot counts is greater than 0.
        '''

        gameObject.play(1000)
        analyzerObject = Analyzer(gameObject)
        self.assertGreater(analyzerObject.jackpot(),0)


    def test_7_ANALYZER_combo(self):

        '''
        The analyzer object has been created by inputting the game object as the input parameter.
        This test checks that the combo method has run correctly, by summing the frequency column in the combo dataframe.
        Returns "ok" if the sum is equal to the total number of rolls.
        '''

        gameObject.play(1000)
        analyzerObject = Analyzer(gameObject)
        analyzerObject.combo()
        self.assertEqual(analyzerObject.comboDF['frequencies'].sum(),1000)

    def test_8_ANALYZER_facecounts(self):

        '''
        The analyzer object has been created by inputting the game object as the input parameter.
        This test checks that the combo method has run correctly,
         by ensuring that the number of rolls in the returned dataframe is equal to the number of times the die were rolled in the game.
        Returns "ok" if the nuymber of rolls in the facecounts dataframe is equal to 1000.
        '''

        gameObject.play(1000)
        analyzerObject = Analyzer(gameObject)
        analyzerObject.facecountsperroll()
        self.assertEqual(len(analyzerObject.facecountsDF), 1000)




if __name__ == '__main__':
    dieObject = Die([1,2,3,4,5,6])
    gameObject = Game([dieObject, dieObject])
    unittest.main(verbosity=3)