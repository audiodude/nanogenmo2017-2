import random


def generate_id():
  id_ = 0
  while True:
    yield id_
    id_ += 1
get_id = generate_id()

class Model(dict):
  def __init__(self, **kwargs):
    super(Model, self).__init__(**kwargs)
    self.id_ = next(get_id)

  def equals(self, oth):
    return hasattr(oth, 'id_') and self.id_ == oth.id_

class Object(Model):
  pass

class Name(Model):
  pass

class Character(Model):
  def place(self, location):
    self['location'] = location
    location['people_present'].append(self)

class Location(Model):
  def __init__(self, **kwargs):
    super(Location, self).__init__(**kwargs)
    self['transit'] = {}
    self['sublocations'] = []
    self['people_present'] = []

  def transit_link(self, mode, oth_location):
    self['transit'][mode] = oth_location
    oth_location['transit'][mode] = self

  def sublocation(self, oth_location):
    oth_location['sublocations'].append(self)
    self['parent_location'] = oth_location

class Action(Model):
  pass

class Attribute(Model):
  pass

class DomainModel:
  def __init__(self, objects, actions, characters, locations):
    self.objects = objects[:]
    random.shuffle(self.objects)
    self.actions = actions[:]
    random.shuffle(self.actions)
    self.characters = characters[:]
    random.shuffle(self.characters)
    self.locations = locations[:]
    random.shuffle(self.locations)
