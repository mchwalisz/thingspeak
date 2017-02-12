import pytest
import os
import vcr
import logging
from collections import namedtuple

logging.basicConfig()
vcr_log = logging.getLogger("vcr")
vcr_log.setLevel(logging.INFO)

descr = namedtuple('ChannelParam', 'id access api_key write')

channels = [
    descr(id=int(os.environ.get('THINGSPEAK_ID_PUBLIC', '86945')),
        access='public',
        api_key=os.environ.get('THINGSPEAK_KEY_PUBLIC',
            'XXXXXXXXXXXXXXXX'),
        write=True),
    descr(id=int(os.environ.get('THINGSPEAK_ID_PRIVATE', '204504')),
        access='private',
        api_key=os.environ.get('THINGSPEAK_KEY_PRIVATE_WRITE',
            'XXXXXXXXXXXXXXXX'),
        write=True),
    descr(id=int(os.environ.get('THINGSPEAK_ID_PRIVATE', '204504')),
        access='private',
        api_key=os.environ.get('THINGSPEAK_KEY_PRIVATE_READ',
            'YYYYYYYYYYYYYYYY'),
        write=False),
]

channels_ids = [
    'public',
    'private_write',
    'private_read',
]


@pytest.fixture(
    params=channels, ids=channels_ids)
def channel_param(request):
    yield request.param


def replace_auth(key, value, request):
    for ch_id, channel in zip(channels_ids, channels):
        if channel.api_key == value:
            return ch_id
    else:
        return value


vcr.default_vcr = vcr.VCR(
    record_mode='new_episodes' if os.environ.get('CI') == 'true' else 'none',
    cassette_library_dir='tests/cassettes',
    path_transformer=vcr.VCR.ensure_suffix('.yaml'),
    filter_query_parameters=[('api_key', replace_auth)],
)
vcr.use_cassette = vcr.default_vcr.use_cassette
