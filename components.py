import random

import messages
import models

class DocumentPlanner:
  def __init__(self, domain_model):
    self.domain_model = domain_model
    self.messages = []

  def run(self):
    self.main_character = self.domain_model.characters[0]

    self.location = self.main_character['location']
    self.describe_character(self.main_character)
    self.describe_character_location(self.main_character)
    self.describe_location(self.location)

  def describe_character(self, c):
    msg = messages.DescribeCharacterMsg(character=c)
    msg.append(models.Attribute(txt='%s year old' % c['age']))
    msg.append(
      models.Attribute(txt='man' if c['gender'] == 'male' else 'woman'))
    self.messages.append(msg)

  def describe_character_location(self, c):
    msg = messages.DescribeCharacterLocationMsg(
      character=c, location=c['location'])
    self.messages.append(msg)

  def describe_location(self, l):
    self.messages.append(messages.DescribeLocationMsg(location=l))
    self.describe_random_objects_in_location(l)

  def describe_random_objects_in_location(self, l):
    n_obj = len(l['objects_present'])
    n_to_desc = n_obj
    if n_obj > 4:
      n_to_desc = random.randint(1, n_obj // 2)
    objs = l['objects_present'][:]
    objs = objs[:n_to_desc]
    random.shuffle(objs)
    for i, o in zip(range(n_to_desc), objs):
      self.messages.append(
        messages.DescribeObjectLocationMsg(obj=o, location=l))
