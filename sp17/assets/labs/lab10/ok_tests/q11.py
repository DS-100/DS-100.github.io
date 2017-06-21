test = {
  'name': 'Question 15',
  'points': 1,
  'suites': [
    {
      'cases': [
        {  
          'code': r"""
          >>> np.max(np.abs(X_people_perturbed - noise - X_people)) < 1e-5
          True
          >>> np.max(np.abs(theta_people_perturbed - sc.linalg.inv(X_people_perturbed.T @ X_people_perturbed) @ X_people_perturbed.T @ Y_people)) < 1e-5
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
