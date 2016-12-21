import sys
import json
import vcr
import pytest
import requests
from thingspeak import Channel

import logging

logging.basicConfig()
vcr_log = logging.getLogger("vcr")
vcr_log.setLevel(logging.INFO)

ts_vcr = vcr.VCR(
    record_mode='new_episodes',
    cassette_library_dir='tests/cassettes',
    path_transformer=vcr.VCR.ensure_suffix('.yaml'),
    filter_query_parameters=[('api_key', 'THINGSPEAK_KEY')],
)


@pytest.mark.xfail(sys.version_info < (3, 3),
                   reason="python3.3 api changes")
def test_missing_id():
    with pytest.raises(TypeError) as excinfo:
        Channel()
    assert 'missing 1 required positional argument' in str(excinfo.value)


def test_channel(channel_param):
    ch = Channel(channel_param.id)
    assert ch.id == channel_param.id
    assert ch.api_key is None
    assert ch.server_url == 'https://api.thingspeak.com'
    ch = Channel(channel_param.id, api_key=channel_param.api_key)
    assert ch.api_key is channel_param.api_key


@ts_vcr.use_cassette()
def test_get_with_key(channel_param):
    ch = Channel(id=channel_param.id, api_key=channel_param.api_key)
    result = json.loads(ch.get())
    assert type(result) == dict


@ts_vcr.use_cassette()
def test_get_without_key(channel_param):
    ch = Channel(id=channel_param.id)
    print(ch.api_key)
    if channel_param.access == 'private':
        with pytest.raises(requests.exceptions.HTTPError) as excinfo:
            ch.get()
        excinfo.match(r'400 .*')
    else:
        result = json.loads(ch.get())
        assert type(result) == dict


@ts_vcr.use_cassette()
def test_get_wrong_key(channel_param):
    if channel_param.access == 'public':
        pytest.skip()
    ch = Channel(id=channel_param.id, api_key='wrong key')
    with pytest.raises(requests.exceptions.HTTPError) as excinfo:
        ch.get()
    excinfo.match(r'400 .*')
