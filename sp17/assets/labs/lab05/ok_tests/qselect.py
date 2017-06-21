test = {
  'name': 'Completion',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> select(young_sailors, lambda x: x["rating"] > 6).shape
          (2, 4)
          >>> ssum = select(young_sailors, lambda x: x["rating"] > 6).sname.sum()
          >>> ssum == "JerryJack" or ssum == "JackJerry"
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
