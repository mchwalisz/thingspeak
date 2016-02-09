#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
thingspeak: Channel showcase

Usage:
   thingspeak [options] [-q | -v] <channel>
   thingspeak [options] [-q | -v] <channel> (<field> <value>)...
   thingspeak --config

Arguments:
   <channel>              ThingSpeak Channel ID
   <field>                Field to write to
   <value>                Value to write

Options:
   --api-key=<key>        Read API key for selected channel
                          (no key required for public channels)
   --write-key=<wkey>     Write API key for selected channel
   -r=<r>, --results <r>  Number of results to output
   -f <format>            Output data format [default: json]

Other options:
   --config            prints empty config file
   -c=<conf>           loads config file
   -C                  loads config from ~/.config/thingspeak.json
   -h, --help          show this help message and exit
   -q, --quiet         print less text
   -v, --verbose       print more text
   --version           show version and exit
"""

# import thingspeak as ts
import __init__ as ts
from docopt import docopt
import logging
import json


def main():
    """Run the code for thingspeak"""
    args = docopt(__doc__, version=ts.__version__)
    args = parse_json_config(args)
    log_level = logging.INFO  # default
    if args['--verbose']:
        log_level = logging.DEBUG
    elif args['--quiet']:
        log_level = logging.ERROR
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    log = logging.getLogger('thingspeak.main')
    log.debug(args)
    # Create channel class
    ch = ts.Channel(
        args['<channel>'],
        api_key=args['--api-key'],
        write_key=args['--write-key'],
        fmt=args['-f'],
    )
    opts = dict()
    # Act on channel
    if args['<field>']:
        data = {k: v for k, v in zip(args['<field>'], args['<value>'])}
        print(ch.update(data))
    if args['--results'] is not None:
        opts['results'] = args['--results']
        results = ch.get(opts)
        if args['-f'] == 'json':
            print(json.dumps(json.loads(results), sort_keys=True, indent=2))
        else:
            print(results)
    else:
        print(ch.view())
# def main


def parse_json_config(args):
    """
    Takes care of the correct configure file management.

    It either prints the empty json config structure or adds the
    parameters from the given one to the existing arguments (args)
    """
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
        return dict(
            (str(key), args.get(key) or json_config.get(key))
            for key in set(json_config) | set(args)
        )
    if args['-c']:
        return merge_configs(args, args['-c'])
    elif args['-C']:
        return merge_configs(args, "~/.config/thingspeak.json")
    else:
        return args
# def parse_json_config


if __name__ == "__main__":
    main()
