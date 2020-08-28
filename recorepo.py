#!/usr/bin/python3

import argparse
import re
import requests
import subprocess


def redirect_origin(path, ssh_url):
    print('Redirecting', path, 'to', ssh_url)
    subprocess.run(['git', '-C', path, 'remote', 'set-url', 'origin', ssh_url])
    subprocess.run(['git', '-C', path, 'push', '-u', 'origin', 'master'])

def create_repo(token, name, init, private, https):
    print('Creating respository', name)
    r = requests.post('https://api.github.com/user/repos',
                      headers={'Authorization': 'token {}'.format(token)},
                      json={'name': name, 'auto_init': init, 'private': private})
    response = r.json()
    if r.status_code != 201:
        raise Exception(response['message'])
    if https:
        return response['html_url']
    return response['ssh_url']

def main():
    for path in args.paths:
        repo_name = args.course_code + '-' + path
        try:
            url = create_repo(args.token, repo_name, args.init, not args.public, args.https)
            redirect_origin(path, url)
            print('---------------------------------------------------------------------')
        except Exception as e:
            print(e)

def course_code_type(value, pattern=re.compile(r'^[0-9]{4}$')):
    if not pattern.match(value):
        raise argparse.ArgumentTypeError('Course code {} is not a 4-digit code'.format(value))
    return value

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Redirect git repositories')
    parser.add_argument('token', help='GitHub OAuth token')
    parser.add_argument('course_code', type=course_code_type, help='A 4-digit course code')
    parser.add_argument('paths', nargs='+', help='Repositories to redirect')
    parser.add_argument('-p', '--public', action='store_true', help='Make the repository public. Private by default')
    parser.add_argument('-i', '--init', action='store_true', help='Initialise repository upon creation')
    parser.add_argument('--https', action='store_true', help='Redirect repository to have HTTPS origin path. Uses SSH by default')

    args = parser.parse_args()
    main()
