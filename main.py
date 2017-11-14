import random

import messages
import models
from components import DocumentPlanner, Microplanner, Realizer

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

model = models.DomainModel([eggs], [sleep, get_eggs], [henry], [home, store])
dp = DocumentPlanner(model)
dp.run()

microplanner = Microplanner(dp.messages)
microplanner.run()

realizer = Realizer(microplanner.text_specification)
realizer.run()

print(realizer.text)
