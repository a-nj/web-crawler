from lxml import html
import requests


class GadgetCrawler:
    """docstring for MitCrawler"""

    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.Gadgets = []

    def crawl(self):
        self.get_app_from_link(self.starting_url)
        return

    def get_app_from_link(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)

        name = tree.xpath('//span[@id="ContentPlaceHolder1_lblItemTitle"]/text()')[0]
        price = tree.xpath('//span[@id="ContentPlaceHolder1_rptGheymat_lblGheymat_0"]/text()')[0]

        gadget=Gadget(name,price)
        self.Gadgets.append(gadget)


        return


class Gadget:
    """docstring for Gadget"""

    def __init__(self, name, price):
        self.name = name
        self.price = price


    def __str__(self):
        return ("Name: " + self.name.encode('UTF-8') +
                "\r\nPrice: " + self.price.encode('UTF-8') + "\r\n")


crawler = GadgetCrawler(
    'http://meghdadit.com/product/10618/samsung-galaxy-s7-edge-sm-g935fd-lte-32gb-dual-sim-mobile-phone/%DA%AF%D9%88%D8%B4%DB%8C-%D9%85%D9%88%D8%A8%D8%A7%DB%8C%D9%84-%D8%B3%D8%A7%D9%85%D8%B3%D9%88%D9%86%DA%AF-%DA%AF%D9%84%DA%A9%D8%B3%DB%8C-%D8%A7%D8%B3-7-%D8%A7%D8%AC-%D8%A8%D8%A7-%D9%82%D8%A7%D8%A8%D9%84%DB%8C%D8%AA-4-%D8%AC%DB%8C-32-%DA%AF%DB%8C%DA%AF%D8%A7%D8%A8%D8%A7%DB%8C%D8%AA-%D8%AF%D9%88-%D8%B3%DB%8C%D9%85-%DA%A9%D8%A7%D8%B1%D8%AA/',
    0)
crawler.crawl()

for Gadget in crawler.Gadgets:
    print Gadget