test = {
  'name': 'Question 9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> theta14.shape[0] >= 100
          True
          >>> 150 < (max(theta14) - min(theta14)) < 250
          True
          >>> np.std(theta14 - true_theta_big) < 1
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
