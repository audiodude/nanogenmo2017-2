class Message:
  pass

class WentSomewhereMsg(Message):
  def __init__(self, who=None, where=None, how=None):
    self.who = who
    self.where = where
    self.how = how

class DescribeLocationMsg(Message):
  def __init__(self, location=None):
    self.location = location

class DescribeObjectLocationMsg(Message):
  def __init__(self, obj=None, location=None):
    self.obj = obj
    self.location = location

class DescribeCharacterMsg(Message):
  def __init__(self, character=None):
    self.character = character
    self.attributes = []

  def append(self, attribute):
    self.attributes.append(attribute)

class DescribeCharacterLocationMsg(Message):
  def __init__(self, character=None, location=None):
    self.character = character
    self.location = location
    self.posture = self.character['posture']

class AccomplishGoalMsg(Message):
  def __init__(self, who=None, where=None, action=None):
    self.who = who
    self.where = where
    self.action = action
