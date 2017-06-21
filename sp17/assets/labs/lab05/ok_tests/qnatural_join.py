test = {
  'name': 'Completion',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> all_sailors = union(young_sailors, salty_sailors)
          >>> sailor_reservtions = natural_join(all_sailors, reservations, "sid")
          >>> sailors_and_boats = natural_join(sailor_reservtions, boats, "bid")
          >>> sailor_boats = project(sailors_and_boats, ["sname", "bname", "day"])
          >>> sailor_boats.shape
          (10, 3)
          >>> sailor_boats.apply(lambda x: int(x["day"][2]), axis=1).sum() == 24
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}