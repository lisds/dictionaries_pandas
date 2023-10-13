test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, your dataframe contains the incorrect values...
          >>> np.allclose(totals_per_country['total_Alcohol_deaths_2000_to_2019'].head(5).values, np.array([2415.34,  372.32, 1495.02, 3566.08,   38.66]))
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
