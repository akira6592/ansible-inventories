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
    total: int = 1000
    hosts: dict = {
                    "_meta": {
                        "hostvars": {}
                    },
                    "group001": {"hosts": []}
    }

    for i in range(total):
        hosts["group001"]["hosts"].append("sv" + str(i + 1))

    return hosts

def generate_hosts3() -> dict:

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
        # "_meta": {"hostvars": {}},
        "group001": {
            "hosts": ["host001", "host002"],
            "vars": {"group001_var1": "Hello"},
            "children": ["group002"]
        },
        "group002": {
            "hosts": ["host003"],
            "vars": {"group002_var1": "Hello"}
        }
    }

    return hosts

if args.requested_host:
    # --host
    # print(json.dumps(generate_hosts().get(args.requested_host, {})))
    pass
elif args.list_instances:
    # --list
    print(json.dumps(generate_hosts()))
else:
    raise Exception('I do not know what to do.')

