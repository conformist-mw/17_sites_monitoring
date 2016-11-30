import requests
from whois import whois
from datetime import datetime, timedelta
import argparse


def load_urls4check(filepath):
    with open(filepath, 'r') as f:
        return [url.strip() for url in f]


def is_server_respond_with_200(url):
    return requests.get(url).status_code == 200


def is_domain_expiration_date(domain_name, days=30):
    in_a_month = datetime.now() + timedelta(days=days)
    exp_date = whois(domain_name).get('expiration_date')
    exp_date = exp_date[0] if isinstance(exp_date, list) else exp_date
    if exp_date:
        return in_a_month < exp_date


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Check site health')
    parser.add_argument('filepath', help='path to file with urls')
    args = parser.parse_args()
    for url in load_urls4check(args.filepath):
        if is_server_respond_with_200(url) and is_domain_expiration_date(url):
            print('{:50}{}'.format(url, '\033[92mOK\033[0m'))
        else:
            print('{:50}{}'.format(url, '\033[91mFAIL\033[0m'))
