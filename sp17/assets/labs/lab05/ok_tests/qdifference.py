test = {
  'name': 'Completion',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> difference(young_sailors, salty_sailors).shape
          (3, 4)
          >>> difference(young_sailors, salty_sailors).age.sum() == 74
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