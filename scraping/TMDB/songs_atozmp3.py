#! /usr/bin/env /usr/bin/python3.5

import sys
import requests
from pprint import pprint
from html.parser import HTMLParser
import logging
import time

logging.basicConfig(filename='web_parser.log',level=logging.INFO)

BASE_URL = r'http://www.atozmp3.in'
BASE_EXT = r'/category/telugu-songs-download/page/'

try:
    OP_FILE = open(r'movie_links.log', 'a')
except Exception:
    sys.stderr.write("Problem with op file")
    sys.exit(1)

class AtoZMP3HTMLParser(HTMLParser):
    """
    Handling only start tags which have attribute are 3 only.
    """
    def handle_starttag(self, tag, attrs):
        if len(attrs) == 3:
            dict_content = dict(attrs)
            try:
                if dict_content['rel'] == 'bookmark':
                    OP_FILE.write(dict_content['href'] + "\n")
            except KeyError as e:
                logging.error(str(e) + " for " + str(attrs))

if __name__ == '__main__':
    parser = AtoZMP3HTMLParser()
    start_timer = time.time()
    for i in range(1, 166):
        URL = BASE_URL + BASE_EXT + str(i)
        before = time.time()
        content = requests.get(BASE_URL + BASE_EXT + str(i))
        after = time.time()
        logging.info(URL + " took "  + str(after - before) + "secs")
        parser.feed(content.text)
    end_timer = time.time()
    logging.info(" Totally took "  + str(end_timer - start_timer) + "secs")
    
