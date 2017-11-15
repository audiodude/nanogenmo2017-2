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
    msg.append(models.Attribute(text='%s years old' % c['age']))
    if c['gender'] == 'male':
      msg.append(models.Attribute(text='a man'))
    elif c['gender'] == 'female':
      msg.append(models.Attribute(text='a woman'))
    else:
      msg.append(models.Attribute(text='a person'))
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

class Realizer:
  def __init__(self, document_plan):
    self.document_plan = document_plan[:]

  def run(self):
    self.proto_ps = [msg.to_proto_ps() for msg in self.document_plan]
    self.text_specification = [pps for ar in self.proto_ps for pps in ar]
    self.proto_sentences = [str(x) for x in self.text_specification]
    self.text = ' '.join(self.make_sentence(s) for s in self.proto_sentences)

  def make_sentence(self, s):
    return s[0].upper() + s[1:] + '.'
