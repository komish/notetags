# -*- coding utf-8 -*-

from . import __vers__, __name__
import sys
import os
from configparser import ConfigParser
from argparse import ArgumentParser


def read_config(configpath):
    # for now the only value we don't use a default for
    required_keys = ['note_path']
    additional_keys = ['accepted_extensions', 'modifier']
    defaults = {'accepted_extensions': ['.md'],
                'modifier': '@@'}

    parser = ConfigParser()
    parser.read(configpath)
    config = dict(parser.items("DEFAULT"))

    for key in required_keys:
        if key not in config or not config[key]:
            print("Missing required parameter '{}'").format(key)
            sys.exit(4)

    for key in additional_keys:
        if key == 'accepted_extensions':
            # we need to return proper value type here
            config[key] = config[key].split(':')
        elif key not in config.keys() or not config[key]:
            config[key] = defaults[key]

    return config


def generate_config(configpath, homedir):
    print('Generating configuration...')

    if os.path.exists(configpath):
        print('Seems like a configuration file',
              'already exist at {}'.format(configpath))
        print('Please move this file out of',
              'place to generate a new config.')
        return 1
    else:
        print("Creating Directory {} if not exists: ".format(
                                    os.path.dirname(configpath)), end="")
        try:
            if not os.path.exists(os.path.dirname(configpath)):
                os.makedirs(os.path.dirname(configpath))
                print("OK!")
            else:
                print("EXISTS!")
        except Exception as e:
            print("FAILED!")
            print("Exception: ", e)
            return 3

        print("Creating configuration file at {}: ".format(configpath), end="")
        try:
            with open(configpath, 'w') as conf:
                new_config = ConfigParser()
                new_config.set('DEFAULT', 'note_path',
                               '{}/Notes'.format(homedir))
                new_config.set('DEFAULT',
                               'accepted_extensions',
                               '.md:.txt')
                new_config.set('DEFAULT', 'modifier', '@@')
                new_config.write(conf)
            print("OK!")
        except Exception as e:
            print("FAILED!")
            print(e)
            os.remove(configpath)
            return 3
    return 0


def build_arguments():
    long_description = \
        "Utility to assist in handling manually-tagged note files"

    parser = ArgumentParser(
                            description=long_description,
                            add_help=True)
    parser.add_argument('-v', '--version',
                        action='version',
                        version='{} {}'.format(__name__, __vers__))
    # Create subparser
    subparser = parser.add_subparsers()

    # list all tags
    list_parser = \
        subparser.add_parser(
            'list', help='list all tags found in notes')
    list_parser.set_defaults(list=True)

    # search for tags
    search_parser = \
        subparser.add_parser('search', help='search for notes' +
                             'with specified tag')
    search_parser.add_argument('tag', nargs=1)

    # show configuration
    showconfig_parser = \
        subparser.add_parser('showconfig', help='show app' +
                             'configuration details')
    showconfig_parser.set_defaults(showconfig=True)

    # gen configuration
    genconfig_parser = \
        subparser.add_parser('genconfig', help='generate app' +
                             'configuration file')
    genconfig_parser.set_defaults(genconfig=True)

    return parser
