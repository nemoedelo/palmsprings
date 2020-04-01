month_index = int(input("Month index: "))
month_to_season = {
    1: 'WIN',
    2: 'WIN',
    3: 'SPR',
    4: 'SPR',
    5: 'SPR',
    6: 'SUM',
    7: 'SUM',
    8: 'SUM',
    9: 'AUT',
    10: 'AUT',
    11: 'AUT',
    12: 'WIN',
}

month_to_season_list = ['WIN',
                        'WIN',
                        'SPR',
                        'SPR',
                        'SPR',
                        'SUM',
                        'SUM',
                        'SUM',
                        'AUT',
                        'AUT',
                        'AUT',
                        'WIN']

print(month_to_season[month_index])
print(month_to_season_list[month_index - 1])
