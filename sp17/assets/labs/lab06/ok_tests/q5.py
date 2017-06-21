test = {
  'name': 'Question 5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> all(len(answer) == 24 for answer in q5_answers)
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
