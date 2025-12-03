tea_prices_inr = {
    "Masala Chai": 20,
    "Iced Lemon Chai": 25,
    "Ginger Chai": 30,
    "Kadak Chai": 35,
    "Iced Peach Chai": 40
}

print(tea_prices_inr.items()) # gives you a list of tuples (Each tuple is a key-value pair). like --> dict_items([('Masala Chai', 20), ('Iced Lemon Chai', 25), ('Ginger Chai', 30), ('Kadak Chai', 35), ('Iced Peach Chai', 40)])

teac_prices_usd = {tea: price / 88 for tea, price in tea_prices_inr.items() if price >= 28}

print(teac_prices_usd)
#print(type(teac_prices_usd)) --> dict