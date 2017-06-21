test = {
  'name': 'Question 13',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(resamples)
          200
          >>> type(resamples[0])
          pandas.core.frame.DataFrame
          >>> len(resamples[0])
          26
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
