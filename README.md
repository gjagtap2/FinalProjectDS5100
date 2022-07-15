# Metadata

## Monte Carlo Simulator

## Gargee Jagtap



---
# Synopsis

![image](https://user-images.githubusercontent.com/47149519/179243782-1bc8a7ee-9862-465d-931d-397d952811c9.png)
[source](https://cdn.thisiswhyimbroke.com/images/flashing-dungeons-and-dragons-dice-set-dddices-640x533.jpg)

## Installing
To install this package, clone this git repository on your local machine. 
On your terminal navigate to the folder where the repository is and type the following command:

``` python
pip install MonteCarloSimulator
```

## Importing

To import this package type the following code:

``` python
from montecarlo import * 
```


## Creating Dice

A die has N faces and W weights, and can be rolled to select a face. The die has one behavior, which is to be rolled one or more times. Note that what we are referring to as a 'die' can be any discrete random variable associated with a stochastic process - such as flipping a coin or using a deck of cards. Since our weights only apply to single events, we are assuming the events are independent.



To create a die object, use the `init` method by inputting a list of faces with dtype str or int as the input parameter.

``` python
die1 = Die(['H','T','H','T'])
die2 = Die([1,2,3,4])
```



All die faces will have a default weight of 1.0 assigned to it. To change this weight, use the `change_weight` method with parameters for the face you want changed and the new weight you want assigned to it. The new weight you input must have dtype float or have a dtype that can be converted to a float. Note that the weights are just numbers, not a normalized probability distribution.

``` python
die2.change_weight(2,5)
```



To roll the die, use the `rollDie` method to specify how many times you want the die to be rolled. This method defaults to 1 unless you input a different integer. This method computes a random sample from the vector of faces according to the weights, and returns a list of outcomes.

``` python
die2.rollDie(10)
```



To show the user the die's current set of faces and weights (since the latter can be changed), use the `showCurrent` method. This returns the dataframe created in the initializer.

``` python
die2.showCurrent()
```



## Playing Games

A game consists of rolling one or more dice of the same kind one or more times. Each game is initialized with one or more similarly defined dice. This means that each die in a given game has the same number of sides and associated faces, but each die object may have its own weights. The class has a behavior to play a game, i.e. to roll all of the dice a given number of times, and the class keeps the results of its most recent play.



To create a game object, use the `init` method by inputting one or more similarly defined die objects in a list as the input parameter.

``` python
die1 = Die([1,2,3,4,5,6])
die2 = Die([1,2,3,4,5,6])
die2.change_weight(6,5)

game1 = Game([die1, die1, die2, die2])
```



To play the game, use the `play` method with a parameter specifying how many times the dice should be rolled. The results of the play are saved to a private dataframe of shape N rolls by M dice, with the roll number as a named index.

``` python
game1.play(1000)
```



To show the user the results of the most recent play use the `show` method. This method takes a parameter to return the private dataframe to the user in narrow or wide form. 
This parameter defaults to wide form in which the dataframe has a single column index with the roll number, and each die number as a column. The narrow form of the dataframe will have a two-column index with the roll number and the die number, and a column for the face rolled. This parameter should raise an exception of the user passes an invalid option.

``` python
game1.show()
```



## Analyzing Games

An analyzer takes the results of a single game and computes various descriptive statistical properties about it. These properties are available as attributes of an Analyzer object.



To create an analyzer object use the `init` method with a game object as the input parameter. At the initialization time, the method infers the data type of the die faces being used.

``` python
analyzer1 = Analyzer(game1)
```



To compute how many times the game results in all faces being identical use the `jackpot` method. This method returns an integer for the number of time to the user. This method also stores the results as a dataframe of jackpot results as a public attribute with roll number as a named index.

``` python
analyzer1.jackpot()
```



To compute the distinct combinations of faces rolled along with their counts use the `combo` method. The combinations are sorted and saved in a dataframe with a multi-columned index, and this method stores the results as a dataframe in a public attribute.

``` python
analyzer1.combo()
```



To compute the number of times a given face is rolled in each event use the `facecountsperroll` method. For example, if a roll of five dice has all ones, then the counts for this roll would be 5 for the face value '1' and 0 for all other faces.  The dataframe is in wide format( i.e. it has an index of the roll number and face values as columns), and this method stores the results as a dataframe in a public attribute.

``` python
analyzer1.facecountsperroll()
```



---
# API Description

## class Die():

PURPOSE: create a die object by assigning faces and weights

This class is composed of the following methods and attributes:

### init():
- PURPOSE: initialize arguments of faces, weights, and private dataframe

- INPUTS

    - faces (dtype=str or int):  an array of faces

- ATTRIBUTES

    - weights (dtype=float): an array of 1.0 with length equal to length of faces
    - faces

### change_weight():
- PURPOSE: a method to change the weight of a single face

- INPUTS

    - face (dtype=str or int): the face value to be changed
    - new_weight (dtype=float or can be converted into a float): the new weight to be assigned to that face value


### rollDie():
- PURPOSE: a method to roll the die one or more times, random sample of faces according to weights

- INPUTS

    - nrolls (dtype=int): how many times the die is to be rolled

- RETURNS

    - list of outcomes generated by rolling the die nrolls times


### showCurrent():
- PURPOSE: a method to show the user the die's current set of faces and weights

- RETURNS

    - the dataframe created in the initializer with the updated set of weights (if changed) and the associated faces





## class Game():

PURPOSE: play a game by rolling one or more dice of the same kind a given number of times, and the class keeps the result of its most recent play

This class is composed of the following methods and attributes:

### init():
- PURPOSE: initializes arguments of die objects

- INPUTS

    - dieObjects (dtype=list): list of already instantiated one or more similarly defined dice objects
        

### play():
- PURPOSE: a method to play the game by rolling the dice a given number of times

- INPUTS

    - num_rolls (dtype=int):  number of times the dice should be rolled

### show():
- PURPOSE: a method to show the user the results of the most recent play

- INPUTS

    - form (dtype=str): a parameter to return the dataframe in "wide" (default) or "narrow" form

- RETURNS

    -dataframe containing results of game in the specified form



## class Analyzer():

This class is composed of the following methods and attributes:

## init(): 
- PURPOSE: initializes arguments of game objects

- INPUTS

    - dieObjects (dtype=list): list of already instantiated one or more similarly defined dice objects

## jackpot():
- PURPOSE: a method to compute how many times the game resulted in all faces being identical

- RETURNS

    - an integer for the number a times a jackpot was achieved 

## combo():
-  PURPOSE: a method to compute the distinct combinations of faces rolled along with their counts

    - stores the results as a multi-columned index dataframe in a public attribute of sorted combinations

## facecountsperroll():
- PURPOSE:  a method to compute how many times a given face is rolled in each event

    - stores the results as a dataframe in a public attribute with roll number as the index and face values as columns
        

# Manifest

Files in this git repository:

- montecarlo.py
- montecarlo_demo.ipynb
- montecarlo_tests.py
- montecarlo.txt
- FinalProjectSubmissionTemplate.ipynb
- __init__.py
- directory.py
- setup.py
