# -*- coding: utf-8 -*-

import requests


class Channel(object):
    """ThingSpeak channel object"""

    def __init__(
        self,
        id,
        api_key=None,
        fmt="json",
        timeout=None,
        server_url="https://api.thingspeak.com",
    ):
        self.id = id
        self.api_key = api_key
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
        if self.api_key is not None:
            options["api_key"] = self.api_key
        url = "{server_url}/channels/{id}/feeds{fmt}".format(
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
        if self.api_key is not None:
            options["api_key"] = self.api_key
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
        if self.api_key is not None:
            options["api_key"] = self.api_key
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
        if self.api_key is not None:
            options["api_key"] = self.api_key
        url = "{server_url}/channels/{id}/fields/{field}/last_data_age{fmt}"
        url = url.format(
            server_url=self.server_url, id=self.id, field=field, fmt=self.fmt
        )
        r = requests.get(url, params=options, timeout=self.timeout)
        return self._fmt(r)

    def view(self):
        """View a Channel

        `view-a-channel
        <https://de.mathworks.com/help/thingspeak/view-a-channel.html>`_
        """
        options = dict()
        if self.api_key is not None:
            options["api_key"] = self.api_key
        url = "{server_url}/channels/{id}{fmt}".format(
            server_url=self.server_url, id=self.id, fmt=self.fmt
        )
        r = requests.get(url, params=options, timeout=self.timeout)
        return self._fmt(r)

    def update(self, data):
        """Update channel feed.

        `update-channel-feed
        <https://mathworks.com/help/thingspeak/update-channel-feed.html>`_
        """
        if self.api_key is not None:
            data["api_key"] = self.api_key
        else:
            raise ValueError("Missing api_key")
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
