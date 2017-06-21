test = {
  'name': 'Completion',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> cross_product(young_sailors, salty_sailors).shape
          (25, 8)
          >>> cross_product(young_sailors, salty_sailors).age_x.sum() == 605
          True
          >>> cross_product(young_sailors, salty_sailors).age_y.sum() == 790
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
