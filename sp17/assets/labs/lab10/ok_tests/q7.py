test = {
  'name': 'Question 7',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> import sklearn
          >>> type(lin_model7) == sklearn.linear_model.base.LinearRegression
          True
          >>> lin_model7.coef_.shape
          (10,)
          >>> all(lin_model7.coef_ == theta7)
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
