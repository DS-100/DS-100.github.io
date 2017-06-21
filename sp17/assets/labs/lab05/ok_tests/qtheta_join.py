test = {
  'name': 'Completion',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> th_join = theta_join(young_sailors, salty_sailors, lambda x: x["age_x"] > x["age_y"])
          >>> th_join.shape
          (5, 8)
          >>> th_join.age_x.sum() + th_join.age_y.sum() == 247
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