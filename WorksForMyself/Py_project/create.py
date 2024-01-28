from lxml import etree
import glob
with open('prices.txt', 'w', encoding='utf-8') as f:
    for i in range(1, 80):
        files = glob.glob(f'index{i}*.html')
        if files:
            with open(files[0], 'r', encoding='utf-8') as html_file:
                tree = etree.parse(html_file, etree.HTMLParser())
                names = tree.xpath('//sub[@class="item_title"]/text()')
                prices = tree.xpath('//span[@class="item_price"]/text()')
                for name, price in zip(names, prices):
                    f.write(f'{name}, {price}\n')