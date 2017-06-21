test = {
  'name': 'Completion',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> project(salty_sailors, ["sname", "age"]).shape
          (5, 2)
          >>> "sname" in project(salty_sailors, ["sname", "age"]).columns
          True
          >>> "age" in project(salty_sailors, ["sname", "age"]).columns
          True
          >>> "rating" in project(salty_sailors, ["sname", "age"]).columns
          False
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
