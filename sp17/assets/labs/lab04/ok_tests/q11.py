test = {
  'name': 'Question 11',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import pandas as pd
          >>> example_names = pd.DataFrame({"Name": ["Fo", "Lo", "Fa", "Op"], "Gender": ["F", "F", "F", "M"], "Count": [1, 2, 3, 4]})
          >>> pivot_by_ending(example_names)
          Gender  F  M
          Ending      
          a       3  0
          o       3  0
          p       0  4
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
