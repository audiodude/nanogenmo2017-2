import models

class PhraseSpecification:
  pass

class PPSAbstractSyntax(PhraseSpecification):
  def __init__(self, head=None, features=None, subject=None, obj=None,
               predicate=None, modifier=None):
    self.head = head
    self.features = features
    self.subject = subject
    if self.subject:
      self.subject.render_head = True
    self.obj = obj
    self.predicate = predicate
    self.modifier = modifier
    if self.modifier:
      self.modifier.render_head = True
    self.render_head = False

  def __str__(self):
    article = None
    if self.features and self.features.get('definite') is not None:
      if self.features['definite']:
        article = 'the'
      else:
        article = 'a'

    obj_or_mod = None
    if self.obj:
      obj_or_mod = str(self.obj)
    elif self.modifier:
      obj_or_mod = str(self.modifier)

    head = None
    if self.render_head:
      head = str(self.head)

    return ' '.join(str(x)
                    for x in (article, head, self.subject, self.predicate,
                              obj_or_mod)
                    if x)

class CannedText:
  def __init__(self, text=None):
    self.text = text

  def __str__(self):
    return self.text

class ReferringNP:
  def __init__(self, obj=None):
    self.obj = obj

  def __str__(self):
    name = self.obj['name']
    if name.get('proper', True):
      return name['name']
    else:
      return 'the ' + name['name']
