#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # pass 
  total_batches = []
  for ingredient in recipe:
    if ingredient in ingredients.keys():
        if recipe[ingredient] > ingredients[ingredient]:
            return 0
        else:
            batches = ingredients[ingredient] // recipe[ingredient]
            total_batches.append(batches)
    else:
      return 0
  return min(total_batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))