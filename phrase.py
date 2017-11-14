class PhraseSpecification:
  pass

class PSAbstractSyntax(PhraseSpecification):
  def __init__(self, head=None, features=None, subject=None, obj=None,
               predicate=None, modifier=None):
    self.head = head
    self.features = features
    self.subject = subject
    self.obj = obj
    self.predicate = predicate
    self.modifier = modifier

class PPSAbstractSyntax(PhraseSpecification):
  def __init__(self, head=None, features=None, subject=None, obj=None,
               predicate=None, modifier=None):
    self.head = head
    self.features = features
    self.subject = subject
    self.obj = obj
    self.predicate = predicate
    self.modifier = modifier

  def __str__(self):
    return ' '.join(str(x) for x in (
      self.subject, self.head, self.predicate, self.obj) if x)

class CannedText:
  def __init__(self, text=None):
    self.text = text

  def __str__(self):
    return self.text

class ReferringNP:
  def __init__(self, obj=None):
    self.obj = obj

  def __str__(self):
    return self.obj['name']
