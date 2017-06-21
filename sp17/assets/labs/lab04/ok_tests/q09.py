test = {
  'name': 'Question 9',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> import numpy as np
          >>> more_counts = pd.DataFrame({"a": ["A", "B", "C"], "b": [1000, 0, 1000]})
          >>> print(sample_counts_table(more_counts, "b", 100000)["a"].values)
          ['A' 'C']
          >>> np.all(45000 < sample_counts_table(more_counts, "b", 100000)["b"])
          True
          >>> np.all(55000 > sample_counts_table(more_counts, "b", 100000)["b"])
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
