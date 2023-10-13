test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
          {
          'code': r"""
          >>> # Your function is not retrieving the correct rows...
          >>> all((get_year_for_country_func(2009, 'AFG').values == for_marking.loc[9].values)[0])
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
