# Metdata

## Monte Carlo Simulator
## Gargee Jagtap




# Synopsis

## Installing


## Importing

``` python
from montecarlo import * 
```


## Creating Dice

A die has N faces and W weights, and can be rolled to select a face. The die has one behavior, which is to be rolled one or more times. Note that what we are referring to as a 'die' can be any discrete random variable associated with a stochastic process - such as flipping a coin or using a deck of cards. Since our weights only apply to single events, we are assuming the events are independent.



To create a die object, simply insert a list into the die object with dtype str or int.

``` python
die1 = Die(['H','T'])
die2 = Die([1,2])
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


## Analyzing Games





# API Description