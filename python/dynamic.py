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
    # 生成したいホストの台数
    total: int = 4

    # フォーマットとグループの定義
    hosts: dict = {
                    "_meta": {
                        "hostvars": {}
                    },
                    # 奇数グループ
                    "group_odd": {
                        "hosts": [],
                        "vars": {
                            "groupvar_msg": "In group_odd"
                        }
                    },
                    # 偶数グループ
                    "group_even": {
                        "hosts": [],
                        "vars": {
                            "groupvar_msg": "In group_even"
                        }
                    }
    }

    # ホストのループ
    for i in range(total):

        # ホスト連番とホスト名
        host_number = i + 1
        hostname = "host{0:0=4}".format(host_number)

        # 所属グループ
        my_group = "group_even" if host_number % 2 == 0 else "group_odd"

        # グループへの所属
        hosts[my_group]["hosts"].append(hostname)

        # ホスト変数の定義
        hosts["_meta"]["hostvars"][hostname] = {
            "hostvar_msg": "I am " + hostname
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

