#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from notetags import util, mgmt

# GLOBAL VARIALBES
HOMEDIR = os.path.expanduser('~')
APPDIR = '.notetags'
CONFIGFILE = 'config.ini'
SEARCHSTRING = '[\S]*'


def main():
    # assume a config file doesn't exist
    config_found = False

    # build our config-relevant paths
    config_dir = '{}/{}'.format(HOMEDIR, APPDIR)
    config_file = '{}/{}'.format(config_dir, CONFIGFILE)

    # find the configuration file if exists
    if os.path.exists(config_file):
        config_found = True

    # build and capture positional arguments
    parser = mgmt.build_arguments()
    results = parser.parse_args()

    # handle if config not found and request to generate one was not passed
    if not config_found and 'genconfig' not in vars(results).keys():
        print('Configuration file not found in "{}"'.format(config_file))
        print('run the following to generate a base config file.')
        print("\n\t$ {} genconfig".format(os.path.basename(sys.argv[0])))
        print()
        sys.exit(1)

    # generate a config file if requested
    if 'genconfig' in vars(results).keys():
        sys.exit(mgmt.generate_config(config_file, HOMEDIR))

    # read the configuration in place
    config = mgmt.read_config(config_file)

    # handle if user did not pass arguments
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    # all prerun tasks and preflight checks completed
    if 'list' in vars(results).keys():
        print("=== Listing all tags:")
        file_data = util.get_files(config['note_path'],
                                   config['accepted_extensions'])
        tag_data = util.get_tags(file_data, config['modifier'], SEARCHSTRING)
        util.pprint_tags(tag_data)
        sys.exit(0)
    elif 'showconfig' in vars(results).keys():
        print("{:13}".format("Note Path: "), config['note_path'])
        print("{:13}".format("Extensions: "), config['accepted_extensions'])
        print("{:13}".format("Modifier: "), config['modifier'])
        sys.exit(0)
    elif 'tag' in vars(results).keys():
        for tag in vars(results)['tag']:
            print('=== Searching for tag containing: "{}"'.format(tag))
            file_data = util.get_files(config['note_path'],
                                       config['accepted_extensions'])
            found = util.search(file_data, config['modifier'],
                                tag, SEARCHSTRING)
            util.pprint_files(found)
        sys.exit(0)


if __name__ == '__main__':
    sys.exit(main())
