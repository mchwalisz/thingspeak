# -*- coding: utf-8 -*-

import requests


class Channel(object):
    """ThingSpeak channel object"""

    def __init__(
        self,
        id,
        user_api_key=None,
        read_api_key=None,
        write_api_key=None,
        fmt="json",
        timeout=None,
        server_url="https://api.thingspeak.com",
    ):
        self.id = id
        self.user_api_key = user_api_key
        self.read_api_key = read_api_key
        self.write_api_key = write_api_key
        self.fmt = ("." + fmt) if fmt in ["json", "xml"] else ""
        self.timeout = timeout
        self.server_url = server_url

    def get(self, options=None):
        """Get a channel feed.

        `get-a-channel-feed
        <https://mathworks.com/help/thingspeak/get-a-channel-feed.html>`_
        """
        if options is None:
            options = dict()
        if self.read_api_key is not None:
            options["api_key"] = self.read_api_key
        url = "{server_url}/channels/{id}/feeds{fmt}".format(
            server_url=self.server_url, id=self.id, fmt=self.fmt
        )
        r = requests.get(url, params=options, timeout=self.timeout)
        return self._fmt(r)

    def get_last(self, options=None):
        """Get a last entry in channel feed.

        `get-a-channel-feed
        <https://mathworks.com/help/thingspeak/readlastentry.html>`_
        """
        if options is None:
            options = dict()
        if self.read_api_key is not None:
            options["api_key"] = self.read_api_key
        url = "{server_url}/channels/{id}/feeds/last{fmt}".format(
            server_url=self.server_url, id=self.id, fmt=self.fmt
        )
        r = requests.get(url, params=options, timeout=self.timeout)
        return self._fmt(r)

    def get_field(self, field=None, options=None):
        """Get particular field

        `get-channel-field-feed
        <https://mathworks.com/help/thingspeak/get-channel-field-feed.html>`_
        """
        if options is None:
            options = dict()
        if self.read_api_key is not None:
            options["api_key"] = self.read_api_key
        url = "{server_url}/channels/{id}/fields/{field}{fmt}".format(
            server_url=self.server_url, id=self.id, field=field, fmt=self.fmt
        )
        r = requests.get(url, params=options, timeout=self.timeout)
        return self._fmt(r)

    def get_field_last(self, field=None, options=None):
        """To get the age of the most recent entry in a channel's field feed

        `get-channel-field-feed field_last_data
        <https://mathworks.com/help/thingspeak/get-channel-field-feed.html#field_last_data>`_
        """
        if options is None:
            options = dict()
        if self.read_api_key is not None:
            options["api_key"] = self.read_api_key
        url = "{server_url}/channels/{id}/fields/{field}/last{fmt}".format(
            server_url=self.server_url, id=self.id, field=field, fmt=self.fmt
        )
        r = requests.get(url, params=options, timeout=self.timeout)
        return self._fmt(r)

    def get_last_data_age(self, field=None, options=None):
        """Get last result from particular field in text format

        `get-channel-field-feed field_last_data_age
        <https://mathworks.com/help/thingspeak/get-channel-field-feed.html#field_last_data_age>`_
        """
        if options is None:
            options = dict()
        if self.read_api_key is not None:
            options["api_key"] = self.read_api_key
        url = "{server_url}/channels/{id}/fields/{field}/last_data_age{fmt}"
        url = url.format(
            server_url=self.server_url, id=self.id, field=field, fmt=self.fmt
        )
        r = requests.get(url, params=options, timeout=self.timeout)
        return self._fmt(r)

    def view(self):
        """View a Channel

        `view-a-channel
        <https://mathworks.com/help/thingspeak/view-a-channel.html>`_
        """
        options = dict()
        if self.user_api_key is not None:
            options["api_key"] = self.user_api_key
        url = "{server_url}/channels/{id}{fmt}".format(
            server_url=self.server_url, id=self.id, fmt=self.fmt
        )
        r = requests.get(url, params=options, timeout=self.timeout)
        return self._fmt(r)

    def get_api_keys(self):
        """Get Read/Write API Keys a Channel

        `control-a-channel
        <https://se.mathworks.com/help/thingspeak/channel-control.html>`_
        """
        import json
        v_json = self.view()
        v = json.loads(v_json)
        read_api_key = None
        write_api_key = None
        for k in v['api_keys']:
            if k['write_flag']:
                if write_api_key is None:
                    write_api_key = k['api_key']
            else:
                if read_api_key is None:
                    read_api_key = k['api_key']        
        setattr(self,'read_api_key', read_api_key)
        setattr(self,'write_api_key', write_api_key)
        return read_api_key, write_api_key

    def update(self, data):
        """Update channel feed.

        `update-channel-feed
        <https://mathworks.com/help/thingspeak/update-channel-feed.html>`_
        """
        if self.write_api_key is not None:
            data["api_key"] = self.write_api_key
        else:
            raise ValueError("Missing write api_key")
        url = "{server_url}/update{fmt}".format(
            server_url=self.server_url, id=self.id, fmt=self.fmt
        )
        r = requests.post(url, params=data, timeout=self.timeout)
        return self._fmt(r)

    def _fmt(self, r):
        r.raise_for_status()
        if self.fmt == "json":
            return r.json()
        else:
            return r.text
