test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your correlation coefficient is not correct!
          >>> np.isclose(alc_coca_r, 0.413897930223489, atol = 2)
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
