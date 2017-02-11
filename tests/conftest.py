import pytest
import os
from collections import namedtuple


descr = namedtuple('ChannelParam', 'id access api_key write')

channels = [
    descr(id=int(os.environ.get('THINGSPEAK_ID_PUBLIC', '86945')),
        access='public',
        api_key=os.environ.get('THINGSPEAK_KEY_PUBLIC', 'XXXXXXXXXXXXXXXX'),
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
