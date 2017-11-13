import random


class Model(dict):
  pass

class Object(Model):
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
