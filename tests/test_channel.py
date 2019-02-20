import sys
import json
import vcr
import pytest
import requests
from thingspeak import Channel


@pytest.mark.xfail(sys.version_info < (3, 3), reason="python3.3 api changes")
def test_missing_id():
    with pytest.raises(TypeError) as excinfo:
        Channel()
    assert "missing 1 required positional argument" in str(excinfo.value)


def test_channel(channel_param, servers):
    ch = Channel(channel_param.id, server_url=servers)
    assert ch.id == channel_param.id
    assert ch.api_key is None
    if servers is None:
        ch.server_url == "https://api.thingspeak.com"
    else:
        assert ch.server_url == servers
    ch = Channel(channel_param.id, api_key=channel_param.api_key)
    assert ch.api_key is channel_param.api_key


@vcr.use_cassette()
def test_get_with_key(channel_param):
    ch = Channel(id=channel_param.id, api_key=channel_param.api_key)
    result = json.loads(ch.get())
    assert type(result) == dict


@vcr.use_cassette()
def test_get_without_key(channel_param):
    ch = Channel(id=channel_param.id)
    if channel_param.access == "private":
        with pytest.raises(requests.exceptions.HTTPError) as excinfo:
            ch.get()
        excinfo.match(r"400 .*")
    else:
        result = json.loads(ch.get())
        assert type(result) == dict


@vcr.use_cassette()
def test_get_wrong_key(channel_param):
    if channel_param.access == "public":
        pytest.skip()
    ch = Channel(id=channel_param.id, api_key="wrong_key")
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        ch.get()
    excinfo.match(r"400 .*")


@vcr.use_cassette()
def test_update(channel_param):
    ch = Channel(id=channel_param.id, api_key=channel_param.api_key)
    if channel_param.write:
        ch.update({"field1": 1})
    else:
        with pytest.raises(requests.exceptions.HTTPError) as excinfo:
            ch.update({"field1": 1})
        excinfo.match(r"400 .*")


def test_update_no_key(channel_param):
    ch = Channel(id=channel_param.id)
    with pytest.raises(ValueError) as excinfo:
        ch.update({"field1": 1})
    excinfo.match("Missing api_key")
