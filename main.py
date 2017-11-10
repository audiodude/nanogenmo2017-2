import models


main_character = models.Character(
  name='Fred', gender='male', age=25, transit_modes=[
    'walk', 'bike', 'drive', 'bus'])

home = models.Location(
  name='home', size='building', satisfies=['sleep'], people_present=[],
  objects_present=['bed', 'desk', 'chair', 'bedroom', 'kitchen'])

store = models.Location(
  name='the store', size='building', satisfies=['get eggs'],
  people_present=[{'quantity': 'a few', 'identity': 'anonymous'}],
  objects_present=['eggs'])

