import pytest
import os
from collections import namedtuple


descr = namedtuple('ChannelParam', 'id access api_key write')

channels = [
    descr(id=int(os.environ['THINGSPEAK_ID_PUBLIC']),
        access='public',
        api_key=os.environ['THINGSPEAK_KEY_PUBLIC'],
        write=True),
    descr(id=int(os.environ['THINGSPEAK_ID_PRIVATE']),
        access='private',
        api_key=os.environ['THINGSPEAK_KEY_PRIVATE_WRITE'],
        write=True),
    descr(id=int(os.environ['THINGSPEAK_ID_PRIVATE']),
        access='private',
        api_key=os.environ['THINGSPEAK_KEY_PRIVATE_READ'],
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
