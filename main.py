from common import config
import argparse
from datetime import datetime
import logging
from importlib import import_module

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    site_choices = list(config()['sites'].keys())
    parser.add_argument('site', help='Site to scrape', type=str, choices=site_choices)
    # parser.add_argument('--a', help ='Operation', type=str)    
    # parser.add_argument('--b', help = 'Operation', type=str)
    args = parser.parse_args()

    site = args.site
    # a = args.a
    # b = args.b
    print(f"Starting scraping: {site.capitalize()}")
    archivo = 'src.' + site
    websites = import_module(archivo)

    websites.Site(site)