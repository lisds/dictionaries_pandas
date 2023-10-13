test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Hmmm, either the column names are not correct or you did not use
          >>> # `my_renaming_dict` to do the renaming...
          >>> d, var = for_marking, my_renaming_dict
          >>> correct_names_list = ['Entity', 'Code', 'Year', 'Alcohol use disorders', 'Drug use disorders', 'Opioid use disorders', 'Cocaine use disorders', 'Amphetamine use disorders', 'Other drug use disorders']
          >>> condition_1  = list(d.rename(columns = var).columns) == correct_names_list
          >>> condition_2 = all(substance.columns == correct_names_list)
          >>> condition_1 & condition_2
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
