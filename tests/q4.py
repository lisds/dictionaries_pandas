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
          >>> isinstance(total_alcohol_deaths_for_country, types.LambdaType)
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # Hmmm, your function is not retrieving the correct rows
          >>> np.isclose(total_alcohol_deaths_for_country(country_codes_dict['Russia']), 776220.0599999999)
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
