#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
thingspeak: Does really cool stuff

Usage:
   thingspeak [options] [-q | -v]
   thingspeak --config

Options:
   -f                  foo

Other options:
   --config            prints empty config file
   -c=<conf>           loads config file
   -C                  loads config from ~/.config/thingspeak.json
   -h, --help          show this help message and exit
   -q, --quiet         print less text
   -v, --verbose       print more text
   --version           show version and exit
"""

__author__ = "Mikołaj Chwalisz"

from docopt import docopt
import logging

def main(args):
    """Run the code for thingspeak"""
    log = logging.getLogger('thingspeak.main')
    log.debug(args)
# def main


def parse_json_config(args):
    """
    Takes care of the correct configure file management.

    It either prints the empty json config structure or adds the
    parameters from the given one to the existing arguments (args)
    """
    import json
    if args['--config']:
        del args['-c']
        del args['-C']
        del args['--config']
        del args['--help']
        del args['--quiet']
        del args['--verbose']
        del args['--version']
        print(json.dumps(args, sort_keys=True, indent=4))
        exit()
    def merge_configs(args, filename):
        json_config = json.loads(open(filename).read())
        return dict((str(key), args.get(key) or json_config.get(key))
            for key in set(json_config) | set(args))
    if args['-c']:
        return merge_configs(args, args['-c'])
    elif args['-C']:
        return merge_configs(args, "~/.config/thingspeak.json")
    else:
        return args
# def parse_json_config

if __name__ == "__main__":
    args = docopt(__doc__, version=__version__)
    args = parse_json_config(args)

    log_level = logging.INFO  # default
    if args['--verbose']:
        log_level = logging.DEBUG
    elif args['--quiet']:
        log_level = logging.ERROR
    logging.basicConfig(level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    main(args)
