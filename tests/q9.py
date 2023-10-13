test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Your new column contains the wrong values!
          >>> substance[substance['Code'] == 'AFG']["Cocaine use disorders"].sum() == totals_per_country_sorted_by_alc[totals_per_country_sorted_by_alc['Code'] == 'AFG']['total_Cocaine_deaths_2000_to_2019'].values[0]
          True

          """,
          'hidden': False,
          'locked': False
        },


                {
          'code': r"""
          >>> # Your new column contains the wrong values!
          >>> substance[substance['Code'] == 'RUS']["Cocaine use disorders"].sum() == totals_per_country_sorted_by_alc[totals_per_country_sorted_by_alc['Code'] == 'RUS']['total_Cocaine_deaths_2000_to_2019'].values[0]
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
