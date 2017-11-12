import random

import messages
import models


eggs = models.Object(name='eggs')

sleep = models.Action(name='sleep', transitive=False)
get_eggs = models.Action(name='get eggs', transitive=True, obj=eggs)

henry = models.Character(
  name='Henry', gender='male', age=25, transit_modes=[
    'walk', 'bike', 'drive', 'bus'], posture='standing', desires=[get_eggs])

home = models.Location(
  name='home', size='building', satisfies=[],
)
bedroom = models.Location(
  name='bedroom', size='room', satisfies=[sleep],
  objects_present=[
    models.Object(name='bed'), models.Object(name='desk'), 
    models.Object(name='chair'),
  ]
)
bedroom.sublocation(home)

store = models.Location(
  name='the store', size='building', satisfies=[get_eggs],
  people_present=[{'quantity': 'a few', 'identity': 'anonymous'}],
  objects_present=[eggs])

henry.place(bedroom)

home.transit_link('walk', store)
home.transit_link('bike', store)
home.transit_link('drive', store)
home.transit_link('bus', store)

class Story:
  def __init__(self, objects, actions, characters, locations):
    self.objects = objects[:]
    random.shuffle(self.objects)
    self.actions = actions[:]
    random.shuffle(self.actions)
    self.characters = characters[:]
    random.shuffle(self.characters)
    self.locations = locations[:]
    random.shuffle(self.locations)
    self.messages = []

  def run(self):
    self.described_objects = set()
    self.described_characters = set()
    self.described_locations = set()

    self.main_character = self.characters[0]

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

s = Story([eggs], [sleep, get_eggs], [henry], [home, store])
s.run()
print(repr(s.messages))
