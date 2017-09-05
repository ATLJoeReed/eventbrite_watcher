#!/usr/bin/python3.6
from watcher import EventbriteWatcher


def test_build_payload():
    watcher = EventbriteWatcher(10, '1234567890', 'test')
    payload = watcher.build_payload('1234567890')
    assert payload == {
        'organizer.id': '1234567890'
    }
