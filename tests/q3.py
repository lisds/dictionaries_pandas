test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, your function is not a lambda function...
          >>> import types  # So we can check for a lambda function.
          >>> isinstance(get_year_for_country, types.LambdaType)
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # Your function is not retrieving the correct rows...
          >>> all((get_year_for_country(2009, 'AFG').values == for_marking.loc[9].values)[0])
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
