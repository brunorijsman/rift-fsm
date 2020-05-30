#!/usr/bin/env python3

import argparse
import subprocess
import sys

ARGS = None

def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description='Ping interface statistics')
    parser.add_argument('source-ns', help='Ping source namespace name')
    parser.add_argument('dest-ns', help='Ping destination namespace name')
    parser.add_argument('stats-ns', help='Interface statistics namespace name')
    args = parser.parse_args()
    return args

def fatal_error(error_msg):
    print(error_msg, file=sys.stderr)
    sys.exit(1)

def ping_interface_stats(source_ns, dest_ns, stats_ns):
    if not namespace_exists(source_ns):
        fatal_error("Source namespace {} does not exist".format(source_ns))
    if not namespace_exists(dest_ns):
        fatal_error("Destination namespace {} does not exist".format(dest_ns))
    if not namespace_exists(stats_ns):
        fatal_error("Statistics namespace {} does not exist".format(stats_ns))
    ###@@@

def namespace_exists(ns_name):
    try:
        result = subprocess.run(['ip', 'netns', 'list'], stdout=subprocess.PIPE)
    except FileNotFoundError:
        fatal_error('"ip" command not found')
    output = result.stdout.decode('ascii')
    ns_list_with_ids = output.splitlines()
    ns_list = [ns.split()[0] for ns in  ns_list_with_ids]
    return ns_name in ns_list

def main():
    # pylint:disable=global-statement
    global ARGS
    ARGS = parse_command_line_arguments()
    source_ns = getattr(ARGS, 'source-ns')
    dest_ns = getattr(ARGS, 'dest-ns')
    stats_ns = getattr(ARGS, 'stats-ns')
    ping_interface_stats(source_ns, dest_ns, stats_ns)

if __name__ == "__main__":
    main()
