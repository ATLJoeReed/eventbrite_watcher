#!/usr/bin/python3.6
import datetime
import time

import requests
from twilio.rest import Client

from config import settings


class EventbriteWatcher(object):
    """
    This class is used to watch Eventbrite for new events at a specified
    organization.
    """
    def __init__(self, watch_time, organizer_id, keyword):
        """
        Args:
        __watch_time__: Amount of time to watch for the event.
        __organizer_id__: The ID of the organization to watch.
        __keyword__: Keyword to alert on.
        """
        self.watch_time = watch_time
        self.organizer_id = organizer_id
        self.keyword = keyword

    def build_headers(self, oauth_token):
        token = "Bearer {}".format(oauth_token)
        return {'Authorization': token}

    def build_payload(self, organizer_id):
        return {'organizer.id': organizer_id}

    def check_events(self, events, keyword):
        results = []
        for event in events:
            event_name = event['name']['text']
            event_url = event.get('url', None)
            if keyword.lower() in event_name.lower():
                results.append(event_url)
        return results

    def fetch_events(self):
        response = requests.get(
            settings.BASE_URL,
            headers=self.build_headers(settings.OAUTH_TOKEN),
            params=self.build_payload(self.organizer_id),
        )
        response_status_code = response.status_code
        if response_status_code != 200:
            self.send_sms(
                'Bad response status code: {}'.format(response_status_code)
            )
            return None
        r = response.json()
        return r.get('events', None)

    def get_end_time(self, watch_time):
        return datetime.datetime.now() + \
            datetime.timedelta(minutes=watch_time)

    def send_sms(self, message):
        twilio = settings.TWILIO
        client = Client(
            twilio.get('account_sid', None),
            twilio.get('auth_token', None),
        )
        response = client.messages.create(
            to=twilio.get('to_number', None),
            from_=twilio.get('from_number', None),
            body=message,
        )
        return response

    def start_watching(self):
        self.send_sms('Starting to watch...')
        results_found = 0
        no_events_found = 0
        end_time = self.get_end_time(self.watch_time)
        while results_found < 3 and datetime.datetime.now() < end_time:
            events = self.fetch_events()
            if not events:
                no_events_found += 1
                if no_events_found > 24:
                    self.send_sms('No events found in past 2 hours...')
                    no_events_found = 0
            else:
                results = self.check_events(events, self.keyword)
                if results:
                    results_found += 1
                    for result in results:
                        self.send_sms(result)
            time.sleep(300)
