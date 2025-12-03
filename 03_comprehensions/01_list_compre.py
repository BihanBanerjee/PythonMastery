menu = [
    'Masala Chai',
    'Iced Lemon Chai',
    'Ginger Chai',
    'Kadak Chai',
    'Iced Peach Chai'
]

iced_tea = [tea for tea in menu if 'Iced' in tea]

print(iced_tea)

long_tea = [tea for tea in menu if len(tea) >= 12]

print(long_tea)