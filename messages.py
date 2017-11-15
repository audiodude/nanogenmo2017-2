import phrase

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

  def to_ps(self):
    return [phrase.PSAbstractSyntax(
      head='be', subject=phrase.ReferringNP(obj=self.location),
      predicate=phrase.CannedText(
        text='was the size of a %s' % self.location['size'])
    )]

class DescribeObjectLocationMsg(Message):
  def __init__(self, obj=None, location=None):
    self.obj = obj
    self.location = location

  def to_ps(self):
    mod = phrase.PSAbstractSyntax(
      head='in', obj=phrase.ReferringNP(obj=self.location))
    return [phrase.PSAbstractSyntax(
      head='be', subject=phrase.ReferringNP(obj=self.obj),
      predicate=phrase.CannedText(text='was'),
      modifier=mod, features={'tense': 'past'})]

class DescribeCharacterMsg(Message):
  def __init__(self, character=None):
    self.character = character
    self.attributes = []

  def append(self, attribute):
    self.attributes.append(attribute)

  def to_ps(self):
    proto_ps = []
    for attr in self.attributes:
      proto_ps.append(phrase.PSAbstractSyntax(
        head='be', subject=phrase.ReferringNP(obj=self.character),
        predicate=phrase.CannedText(text='was'),
        obj=phrase.CannedText(text=attr['text']
      )))
    return proto_ps

class DescribeCharacterLocationMsg(Message):
  def __init__(self, character=None, location=None):
    self.character = character
    self.location = location
    self.posture = self.character['posture']

  def to_ps(self):
    mod = phrase.PSAbstractSyntax(
      head='in', obj=phrase.ReferringNP(obj=self.location))
    return [phrase.PSAbstractSyntax(
      head=self.posture, subject=phrase.ReferringNP(obj=self.character),
      modifier=mod, predicate=phrase.CannedText(text='was %s' % self.posture),
      features={'tense': 'past continuous'})]

class AccomplishGoalMsg(Message):
  def __init__(self, who=None, where=None, action=None):
    self.who = who
    self.where = where
    self.action = action
