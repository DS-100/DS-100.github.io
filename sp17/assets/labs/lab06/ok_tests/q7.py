test = {
  'name': 'Question 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> names = {'Daniel', 'Henry', 'Kelly', 'Natalie', 'Sarah', 'Sam'}
          >>> all([name[0] in names for name in q7_answer])
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