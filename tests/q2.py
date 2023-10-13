test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, your dictionary keys are not correct...
          >>> all(list(country_codes_dict.keys()) == substance['Entity'].unique())
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # Hmmm, your dictionary values are not correct...
          >>> all(list(country_codes_dict.values()) == substance['Code'].unique())
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
