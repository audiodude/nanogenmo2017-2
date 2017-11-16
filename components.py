import random

import messages
import models
import phrase

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
    if n_obj >= 4:
      n_to_desc = random.randint(1, n_obj // 2)
    objs = l['objects_present'][:]
    objs = objs[:n_to_desc + 1]
    random.shuffle(objs)
    for i, o in enumerate(objs):
      self.messages.append(
        messages.DescribeObjectLocationMsg(obj=o, location=l))

class Realizer:
  def __init__(self, document_plan):
    self.document_plan = document_plan[:]

  def run(self):
    self.ps = [msg.to_ps() for msg in self.document_plan]
    self.ps = [ps for ar in self.ps for ps in ar]

    self.aggregate()
    self.generate_referring_expressions()

    self.proto_sentences = [str(x) for x in self.ps]
    self.text = ' '.join(self.make_sentence(s) for s in self.proto_sentences)

  def aggregate(self):
    aggregated_ps = []
    last_ps = None
    combined = False
    for ps in self.ps:
      if last_ps is None:
        last_ps = ps
        continue

      if combined:
        combined = False
        last_ps = ps
        continue

      if (ps.subject.equals(last_ps.subject) and
          ps.predicate.equals(last_ps.predicate)):
        combined = True

        ps_obj_str = str(ps.obj)
        lps_obj_str = str(last_ps.obj)

        new_obj = None
        if ps_obj_str.startswith('a ') and not lps_obj_str.startswith('a '):
          if 'years old' in lps_obj_str:
            lps_obj_str = lps_obj_str.replace('years old', 'year old')
          new_obj = phrase.CannedText(
            text=ps_obj_str.replace('a ', 'a %s ' % lps_obj_str))
        elif lps_obj_str.startswith('a ') and not ps_obj_str.startswith('a '):
          if 'years old' in ps_obj_str:
            ps_obj_str = ps_obj_str.replace('years old', 'year old')
          new_obj = phrase.CannedText(
            text=lps_obj_str.replace('a ', 'a %s ' % ps_obj_str))
        else:
          new_obj = phrase.CannedText(text=ps_obj_str + ' and ' + lps_obj_str)

        new_ps = phrase.PSAbstractSyntax(
          subject=ps.subject, predicate=ps.predicate, obj=new_obj)
        aggregated_ps.append(new_ps)
      else:
        combined = False
        aggregated_ps.append(last_ps)
      last_ps = ps
    if not combined:
      aggregated_ps.append(last_ps)
    self.ps = aggregated_ps

  def generate_referring_expressions(self):
    pass

  def make_sentence(self, s):
    return s[0].upper() + s[1:] + '.'
