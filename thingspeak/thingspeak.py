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

from docopt import docopt
import logging
import requests

__author__ = "Mikołaj Chwalisz"
__version__ = "0.2.0"

thingspeak_url = 'https://api.thingspeak.com/'


class Channel(object):
    """ThingSpeak channel object"""
    def __init__(self, id, api_key=None, write_key=None, fmt='json'):
        self.id = id
        self.api_key = api_key
        self.write_key = write_key
        self.fmt = ('.' + fmt) if fmt in ['json', 'xml'] else ''

    def get(self, options=dict()):
        """Get a channel feed.

        Full reference:
        https://de.mathworks.com/help/thingspeak/get-a-channel-feed.html
        """
        if self.api_key is not None:
            options['api_key'] = self.api_key
        url = '{ts}/channels/{id}/feeds{fmt}'.format(
            ts=thingspeak_url,
            id=self.id,
            fmt=self.fmt,
        )
        r = requests.get(url, params=options)
        return self._fmt(r)

    def get_field(self, field=None, options=dict()):
        """Get particular field

        Full reference:
        https://de.mathworks.com/help/thingspeak/get-channel-field-feed.html
        """
        pass

    def view(self):
        """View a Channel"""
        options = dict()
        if self.api_key is not None:
            options['api_key'] = self.api_key
        url = '{ts}/channels/{id}{fmt}'.format(
            ts=thingspeak_url,
            id=self.id,
            fmt=self.fmt,
        )
        r = requests.get(url, params=options)
        return self._fmt(r)
    # def view

    def update(self, data):
        """Update channel feed.

        Full reference:
        https://de.mathworks.com/help/thingspeak/update-channel-feed.html
        """
        if self.write_key is not None:
            data['api_key'] = self.write_key
        url = '{ts}/update{fmt}'.format(
            ts=thingspeak_url,
            id=self.id,
            fmt=self.fmt,
        )
        r = requests.post(url, params=data)
        return self._fmt(r)

    def _fmt(self, r):
        r.raise_for_status()
        if self.fmt == 'json':
            return r.json()
        else:
            return r.text


def main():
    """Run the code for thingspeak"""
    args = docopt(__doc__, version=__version__)
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
    ch = Channel(
        args['<channel>'],
        api_key=args['--api-key'],
        write_key=args['--write-key'],
        fmt=args['-f'],
    )
    opts = dict()
    # Act on channel
    if args['<field>']:
        data = {k:v for k,v in zip(args['<field>'],args['<value>'])}
        print(ch.update(data))
    if args['--results'] is not None:
        opts['results'] = args['--results']
        print(ch.get(opts))
    else:
        print(ch.view())
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
