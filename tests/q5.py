test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, dataframe is not the correct length....
          >>> len(totals_per_country) == 184
          True

          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Hmmm, your `Country` column contains the wrong values
          >>> all(totals_per_country['Country'].values == list(country_codes_dict.keys()))
          True

          """,
          'hidden': False,
          'locked': False
        },

                {
          'code': r"""
          >>> # Hmmm, your `Code` column contains the wrong values
          >>> all(totals_per_country['Code'].values == list(country_codes_dict.values()))
          True

          """,
          'hidden': False,
          'locked': False
        },

                        {
          'code': r"""
          >>> # Hmmm, your `totals_per_country` dataframe has the wrong column names
          >>> list(totals_per_country.columns[:2]) == ['Country', 'Code']
          True

          """,
          'hidden': False,
          'locked': False
        },

                                {
          'code': r"""
          >>> # Hmmm, it looks like you didn't use the `dict_to_make_totals_by_country_df` dictionary to construct your dataframe.
          >>> totals_per_country[['Country', 'Code']].equals(pd.DataFrame(dict_to_make_totals_by_country_df))
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
