import os
import requests
from progress.spinner import Spinner
import re
from pathlib import Path
from .services import create_log


def download_file(url):
    response = requests.get(url)
    with open('file.txt', 'wb') as file:
        file.write(response.content)


def delete_file(filename='file.txt'):
    path = Path(__file__).resolve().parent.parent / filename
    os.remove(path)


def parse_apache_log_file(filename='file.txt'):
    pattern = re.compile(r'(?P<ip>[\d\.]+).*\[(?P<date>.*)\] "(?P<method>\w*) (?P<uri>\S*).*" (?P<status>\d*) '
                         r'(?P<response_size>\d*)')
    spinner = Spinner('Parsing     ')
    with open(filename, 'r') as file:
        for line in file:
            if len(line) > 10:
                kwargs = pattern.match(line).groupdict()
                create_log(**kwargs)
                spinner.next()
            print()

