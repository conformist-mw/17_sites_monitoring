import requests
from whois import whois
from monthdelta import monthdelta
from datetime import datetime
import argparse


def load_urls4check(filepath):
    with open(filepath, 'r') as f:
        return [url.strip() for url in f]


def is_server_respond_with_200(url):
    return requests.get(url).status_code == 200


def is_domain_expiration_date(domain_name):
    in_a_month = datetime.now() + monthdelta(1)
    exp_date = whois(domain_name).get('expiration_date')
    if exp_date:
        if not isinstance(exp_date, list):
            return in_a_month < exp_date
        else:
            return in_a_month < exp_date[0]
    else:
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Check site health')
    parser.add_argument('filepath', help='path to file with urls')
    args = parser.parse_args()
    for url in load_urls4check(args.filepath):
        if is_server_respond_with_200(url) and is_domain_expiration_date(url):
            print('{} is OK'.format(url))
        else:
            print('{} have problems'.format(url))
