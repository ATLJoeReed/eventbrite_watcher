#!/usr/bin/python3.6
from watcher import EventbriteWatcher


def test_build_header():
    watcher = EventbriteWatcher(10, '1234567890', 'test')
    header = watcher.build_headers('987654321')
    assert header == {
        'Authorization': 'Bearer 987654321'
    }
