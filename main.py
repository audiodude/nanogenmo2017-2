import random

import messages
import models
from components import DocumentPlanner, Realizer

eggs = models.Object(name='eggs')

sleep = models.Action(name='sleep', transitive=False)
get_eggs = models.Action(name='get eggs', transitive=True, obj=eggs)

henry = models.Character(
  name=models.Name(name='Henry', proper=True), gender='male', age=25,
  transit_modes=['walk', 'bike', 'drive', 'bus'], posture='standing',
  desires=[get_eggs])

home = models.Location(
  name=models.Name(name='home', proper=True), size='building', satisfies=[],
)
bedroom = models.Location(
  name=models.Name(name='bedroom', proper=False), size='room',
  satisfies=[sleep],
  objects_present=[
    models.Object(name=models.Name(name='bed', proper=False)),
    models.Object(name=models.Name(name='desk', proper=False)), 
    models.Object(name=models.Name(name='chair', proper=False)),
  ]
)
bedroom.sublocation(home)

store = models.Location(
  name=models.Name(name='store', proper=False), size='building',
  satisfies=[get_eggs], people_present=[{
    'quantity': 'a few', 'identity': 'anonymous'}],
  objects_present=[eggs])

henry.place(bedroom)

home.transit_link('walk', store)
home.transit_link('bike', store)
home.transit_link('drive', store)
home.transit_link('bus', store)

model = models.DomainModel([eggs], [sleep, get_eggs], [henry], [home, store])
dp = DocumentPlanner(model)
dp.run()

realizer = Realizer(dp.messages)
realizer.run()

print(realizer.text)
