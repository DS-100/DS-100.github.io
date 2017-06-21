test = {
  'name': 'Question 4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> rows7 = {('Joey', 7), ('Henry', 7)}
          >>> rows6 = {('Ian', 6), ('Joyce', 6)}
          >>> q4_answer[0] == ("John", 8)
          True   
          >>> all([tuple(row) in rows7 for row in q4_answer[1:3]])
          True
          >>> all([tuple(row) in rows6 for row in q4_answer[3:5]])
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
