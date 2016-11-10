import pytest
import thingspeak
import responses


@pytest.fixture
def get_channel():
    body = '''
{
  "channel": {
    "created_at": "2010-12-14T01:20:06Z",
    "description": "Netduino Plus connected to sensors around the house",
    "field1": "Light",
    "field2": "Outside Temperature",
    "id": 9,
    "last_entry_id": 11127690,
    "latitude": "40.44",
    "longitude": "-79.9965",
    "name": "my_house",
    "updated_at": "2016-11-10T23:03:02Z"
  },
  "feeds": [
    {
      "created_at": "2016-11-10T23:02:47Z",
      "entry_id": 11127689,
      "field1": "280",
      "field2": "37.197452229299365"
    },
    {
      "created_at": "2016-11-10T23:03:02Z",
      "entry_id": 11127690,
      "field1": "279",
      "field2": "40.764331210191081"
    }
  ]
}
'''
    responses.add(responses.GET,
        'https://api.thingspeak.com//channels/9/feeds.json',
        body=body, status=200, content_type='application/json')
    return body


def test_missing_id():
    with pytest.raises(TypeError) as excinfo:
        thingspeak.Channel()
    assert 'missing 1 required positional argument' in str(excinfo.value)


@responses.activate
def test_get(get_channel):
    ch = thingspeak.Channel(9, fmt='json')
    assert ch.get({'results': 2}) == get_channel
    assert len(responses.calls) == 1
