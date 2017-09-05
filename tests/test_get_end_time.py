import datetime

from watcher import EventbriteWatcher


def test_get_end_time_1(test_minutes=1):
    watcher = EventbriteWatcher(1, '1234567890', 'test')
    current_time = datetime.datetime.now()
    test_time = current_time + datetime.timedelta(minutes=test_minutes)
    end_time = watcher.get_end_time(test_minutes)
    assert end_time.minute == test_time.minute


def test_get_end_time_2(test_minutes=10):
    watcher = EventbriteWatcher(10, '1234567890', 'test')
    current_time = datetime.datetime.now()
    test_time = current_time + datetime.timedelta(minutes=test_minutes)
    end_time = watcher.get_end_time(test_minutes)
    assert end_time.minute == test_time.minute


def test_get_end_time_3(test_minutes=40):
    watcher = EventbriteWatcher(40, '1234567890', 'test')
    current_time = datetime.datetime.now()
    test_time = current_time + datetime.timedelta(minutes=test_minutes)
    end_time = watcher.get_end_time(test_minutes)
    assert end_time.minute == test_time.minute


def test_get_end_time_4(test_minutes=55):
    watcher = EventbriteWatcher(55, '1234567890', 'test')
    current_time = datetime.datetime.now()
    test_time = current_time + datetime.timedelta(minutes=test_minutes)
    end_time = watcher.get_end_time(test_minutes)
    assert end_time.minute == test_time.minute
