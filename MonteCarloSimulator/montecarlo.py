import enchant
import numpy as np
import pandas as pd
from turtle import color
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None




class Die():

    '''
    PURPOSE: create a die object by assigning faces and weights
    '''
    
    
    def __init__(self, faces):

        '''
        PURPOSE: initialize arguments of faces, weights, and private dataframe

        INPUTS
        faces:  an array of faces with dtype strings or numbers

        initializes weights to 1.0 for each face
        saves both faces and weights into a private dataframe that is shared by the other methods
        '''

        self.faces = faces
        self.weights = [1.0 for i in faces]
        self._df = pd.DataFrame({
            'faces': self.faces,
            'weights': self.weights
        })



    def changeWeight(self, face, new_weight):

        '''
        PURPOSE: a method to change the weight of a single face

        INPUTS
        face (dtype=str or int) :        the face value to be changed                    
        new_weight  (dtype=float or can be converted into a float):  the new weight to be assigned to that face value     [float] or [int]

        checks to see if the face passed is valid (in the array of faces)
        checks to see if weight dtype valid (is a float, or can be turned into a float)
        '''

        if (face not in self.faces):
            print("Face value not found. Please enter a valid face value")
        if (type(float(new_weight))!=float):
            print("Please provide weight as a float")
        else:
            self.weights[self.faces.index(face)]=float(new_weight)
            self._df.loc[:,'weights'][self.faces.index(face)]=float(new_weight)



    def rollDie(self, nrolls=1):

        '''
        PURPOSE: a method to roll the die one or more times, random sample of faces according to weights

        INPUTS
        nrolls (dtype=int):  how many times the die is to be rolled 
        
        OUTPUTS
        list of outcomes generated by rolling the die nrolls times
        '''

        outcomes = self._df.faces.sample(n = nrolls, replace=True, weights=self._df.weights)
        return list(outcomes)


    
    def showCurrent(self):

        '''
        PURPOSE: a method to show the user the die's current set of faces and weights

        OUTPUTS
        the dataframe created in the initializer with the updated set of weights (if changed) and the associated faces
        '''
        return self._df





class Game():

    '''
    PURPOSE: play a game by rolling one or more dice of the same kind a given number of times the class keeps the result of its most recent play
    '''

    def __init__(self,dieObjects):

        '''
        PURPOSE: initialize arguments of die objects

        INPUTS
        dieObjects (dtype=list): list of already instantiated one or more similarly defined dice objects
        * each die in a given game has the same number of sides & associated faces, but each die object may have different weights
        
        '''
        self.dieObjects = dieObjects

    
    def play(self, num_rolls):

        '''
        PURPOSE: a method to play the game by rolling the dice a given number of times

        INPUTS
        num_rolls  (dtype=int):  number of times the dice should be rolled

        saves the result of the game to a private dataframe
        
        '''
        
        rollNumber = [i for i in range(1,num_rolls+1)]
        self._dfgame = pd.DataFrame({'rollNumber':rollNumber,}).set_index('rollNumber')
        for i in range(len(self.dieObjects)):
            self._dfgame[i] = (self.dieObjects[i].rollDie(num_rolls))


    def show(self, form = 'wide'):

        '''
        PURPOSE: a method to show the user the results of the most recent play

        INPUTS
        form:  a parameter to return the dataframe in "wide" (default) or "narrow" form  [string]

        OUTPUTS
        _dfgame:  dataframe containing results of game in specified form
        '''

        if form=='wide':
            return self._dfgame
        if form=='narrow':
            self._dfgame = self._dfgame.melt(
                value_vars = [i for i in range(len(self.dieObjects))],
                var_name = 'dieNumber', value_name = 'faceRolled',
                ignore_index=False).reset_index().set_index(['dieNumber','rollNumber'])
            return self._dfgame
        else:
            print("Invalid request, please enter 'narrow' or 'wide'.")



class Analyzer():

    '''
    PURPOSE: takes the result of a single game and computes various descriptive statistical properties about it
    * the properties results are available as attributes of an Analyzer object
    '''

    def __init__(self, gameObject):

        '''
        PURPOSE: initialize arguments of a game object, infers data type of the die faces used

        INPUTS
        gameObject: game object

        saves dataframe of game object to resultsDF
        '''
        self.resultsDF = gameObject.show()

    def jackpot(self):

        '''
        PURPOSE: a method to compute how many times the game resulted in all faces being identical

        stores the results as a dataframe of jackpot results in a public attribute with roll number as a named index

        OUTPUTS:
        an integer for the number a times a jackpot was achieved 

        '''
        self.jackpotResults = self.resultsDF[self.resultsDF.nunique(axis=1).eq(1)]
        return len(self.jackpotResults)


    def combo(self):

        '''
        PURPOSE: a method to compute the distinct combinations of faces rolled along with their counts

        stores the results as a multi-columned index dataframe in a public attribute of sorted combinations
        '''
        #self.comboDF = (self.resultsDF.value_counts()).to_frame(name='frequencies')
        self.comboDF = self.resultsDF.apply(lambda x: pd.Series(sorted(x)), 1)\
            .value_counts().to_frame('frequencies')


    def facecountsperroll(self):

        '''
        PURPOSE: a method to compute how many times a given face is rolled in each event

        stores the results as a dataframe in a public attribute with roll number as the index and face values as columns
        '''
        self.facecountsDF = self.resultsDF.apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)