from watcher import EventbriteWatcher


def test_check_events_1():
    watcher = EventbriteWatcher(1, '1234567890', 'test')
    events = [
        {
            'name': {'text': 'Made in Atlanta'},
            'url': 'www.test.com',
        }
    ]
    results = watcher.check_events(events, 'Made')
    assert results == ['www.test.com']


def test_check_events_2():
    watcher = EventbriteWatcher(1, '1234567890', 'test')
    events = [
        {
            'name': {'text': 'Made in Atlanta'},
            'url': 'www.test.com',
        },
        {
            'name': {'text': 'Made in Atlanta 2'},
            'url': 'www.test2.com',
        },
    ]
    results = watcher.check_events(events, 'Made')
    assert results == ['www.test.com', 'www.test2.com']


def test_check_events_3():
    watcher = EventbriteWatcher(1, '1234567890', 'test')
    events = [
        {
            'name': {'text': 'Started in Atlanta'},
            'url': 'www.test.com',
        }
    ]
    results = watcher.check_events(events, 'Made')
    assert results == []
