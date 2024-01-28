import glob
def get_prices_from_file(filename):
    prices = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.split(',')
            name = parts[0].strip()
            old_price = parts[1].strip()
            new_price = parts[2].strip()
            prices[name] = (old_price, new_price)
    return prices
def replace_price_in_file(filename, prices):
    with open(filename, 'r', encoding='utf-8') as file:
        file_data = file.read()
    for name, (old_price, new_price) in prices.items():
        if name in file_data:
            # Заменить старую цену на новую
            file_data = file_data.replace(str(old_price), str(new_price))
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(file_data)
prices = get_prices_from_file('prices.txt')
for i in range(34, 35):  # цикл от 34 до 35
    for filename in glob.glob(f'ind{i}*.html'): 
        replace_price_in_file(filename, prices)
