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

###listFormat

This uses the import `listFormat`.
It uses a class, and must be instantiated as follows:

```python

variableName = listFormat.Formatter()

```

If you wish to give it an list to start, just put one inbetween the brackets. The list can be added to like so:
```python
variableName.add("List item")
```
To randomize, or scramble, the order of the items in the list, run:
```python
variableName.randomize()
```
To simply take out the raw list, run:
```python
variableName.simpleOutput()
```

Or, to format to a 2D list, use:
```python
variableName.formatOutput(x,y)
```
Where x and y are the width and height of the desired list.

All of the above methods work standalone.

```python
print(listFormat.random()


###confReturn
This is another import, `confReturn`

Very simply, run it like so:

```python
variableName = confReturn.do("gender")
```
Where `"gender"` can be any string being set. Play arround with it in IDLE, you'll get the gist of it.

##Contributions

Financial aid is always welcome at [Paypal](https://www.paypal.me/felixj20000), or of couse feel free to fork the project. If you
do fork, please make pull requests back - I am always looking to improve my work.
