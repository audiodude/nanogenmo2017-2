class Message:
  pass

class WentSomewhereMsg(Message):
  def __init__(self, who=None, where=None, how=None):
    self.who = who
    self.where = where
    self.how = how

class DescribeLocationMsg(Message):
  def __init__(self, location=None, contains=None):
    self.location = location
    self.contains = contains[:] if contains else None

class DescribeObjectMsg(Message):
  def __init__(self, obj=None, location=None):
    self.obj = obj
    self.location = location

class DescribeCharacterMsg(Message):
  def __init__(self, character=None):
    self.character = character

class AccomplishGoalMsg(Message):
  def __init__(self, who=None, where=None, action=None):
    self.who = who
    self.where = where
    self.action = action
