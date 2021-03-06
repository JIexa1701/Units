# -*- coding: utf-8 -*-
"""Класс Battle.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hksolDEmdtqVxu6gJtUnWK5lvPzgxFAH
"""

# Создайте класс, отвечающий за битву юнитов. Опрделите того, кто наносит первый удар, проверйте уровень hp после каждого удара.

import random

class GameObj:
  _name = ''
  _hp = 0

class Unit(GameObj):
  _power = 0
  _defence = 0
  _chance = 0.8

  def __init__(self, name, hp, att, defence):
  # check types here
    self._name = name
    if isinstance(hp, int) and hp > 0:
      self._hp = hp
    if isinstance(att, int):
      self._power = att
    if isinstance(defence, int) or isinstance(defence, float):
      self._defence = defence
    #self.__example = None

class Battle(Unit):
  _place = ''
  _chance_avoid = 0.6

  def __init__(self, name, hp, att, defence):
    super().__init__(name, hp, att, defence)
     
  def fight(self, enemy):
    if type(self) == type(enemy):
      damage = self._power - enemy._defence
    if random.random() > self._chance_avoid:
      enemy._hp -= damage
    if enemy._hp > 0:
      print(f'{self._name} нанес {damage} урона')
    else:
      print(f'{self._name} победил, нанеся {damage} урона')
  
a = Battle('Artur', 20, 3, 1.3)
b = Battle('Lancelot', 15, 5, 0.7) 

who_is_first = ['a', 'b']
if random.choice(who_is_first) == 'a':
  a.fight(b)
else:
  b.fight(a)

while a._hp > 0 and b._hp > 0:
  a.fight(b)  
  if b._hp > 0:              
    b.fight(a)
  if a._hp <= 0 or b._hp <= 0:
    print("Game over")
    break