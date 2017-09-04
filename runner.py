from watcher import EventbriteWatcher


watcher = EventbriteWatcher(540, '6453217513', 'made')
# watcher = EventbriteWatcher(10, '6453217513', 'consumer')

watcher.start_watching()
