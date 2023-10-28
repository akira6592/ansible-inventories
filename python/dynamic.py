#!/usr/bin/env python

'''
This script returns variables specific to a host if given --host <hostname> option
'''

from argparse import ArgumentParser
import json


parser = ArgumentParser()
parser.add_argument(
    '--list', dest='list_instances', action='store_true', default=True,
    help='List instances (default: True)'
)

parser.add_argument(
    '--host', dest='requested_host',
    help='Get all the variables about a specific instance'
)

args = parser.parse_args()

def generate_hosts() -> dict:
    hosts: dict = {
        "_meta": {
            "hostvars": {
                "host001": {
                    "me" : "I am host001"
                },
                "host002": {
                    "me": "I am host002"
                },
                "host003": {
                    "me": "I am host003"
                }
            }
        },
        "group001": {
            "hosts": ["host001", "host002"],
            "vars": {"var1": True},
            "children": ["group002"]
        },
        "group002": {
            "hosts": ["host003"],
            "vars": {"var2": 500}
        }
    }

    return hosts

if args.requested_host:
    # --host
    print(json.dumps(generate_hosts().get(args.requested_host, {})))
elif args.list_instances:
    # --list
    print(json.dumps(generate_hosts()))
else:
    raise Exception('I do not know what to do.')


