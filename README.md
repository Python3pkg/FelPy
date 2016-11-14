# FelPy

## Intro

This is an assortment of Python tools that I have/will write/n, usually because they help me. If something that I've bodged
together can be made to work within 4h of work to a standard I can publish, I'll throw it in here

##Install

These tools are all published as one package, but are all used with seperate import statements. To install:

```bash

sudo pip install FelPy

```

This will install everything automagically.

##Usage

###ArrayFormat

This uses the import `ArrayFormat`.
It uses a class, and must be instantiated as follows:

```python

variableName = ArrayFormatt.Formatter()

```

If you wish to give it an array to start, just put one inbetween the brackets. The array can be added to like so:
```python
variableName.add("Array item")
```
To randomize, or scramble, the order of the items in the array, run:
```python
variableName.randomize()
```
To simply take out the raw array, run:
```python
variableName.simpleOutput()
```

Or, to format to a 2D array, use:
```python
variableName.formatOutput(x,y)
```
Where x and y are the width and height of the desired array.


##Contributions

Financial aid is always welcome at [Paypal](https://www.paypal.me/felixj20000), or of couse feel free to fork the project. If you
do fork, please make pull requests back - I am always looking to improve my work.
