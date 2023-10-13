test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, your dataframe contains the incorrect values...
          >>> np.allclose(totals_per_country_sorted_by_alc['total_Alcohol_deaths_2000_to_2019'].values[:6], np.array([3137042.73, 776220.06, 389930.76, 377845.12, 187186.29, 185218.15])) or np.allclose(totals_per_country_sorted_by_alc['total_Alcohol_deaths_2000_to_2019'].values[:5], np.array([ 776220.06, 389930.76, 377845.12, 187186.29, 185218.15]))
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
