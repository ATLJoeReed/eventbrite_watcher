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

        # Extract setting values...
        self.base_url = settings.BASE_URL
        self.oauth_token = settings.OAUTH_TOKEN
        self.twilio = settings.TWILIO

    def build_headers(self):
        token = "Bearer {}".format(self.oauth_token)
        return {'Authorization': token}

    def build_payload(self):
        return {'organizer.id': self.organizer_id}

    def check_eventbrite(self):
        results = []
        response = requests.get(
            self.base_url,
            headers=self.build_headers(),
            params=self.build_payload(),
            verify=True,
        )
        r = response.json()
        events = r.get('events', None)
        for event in events:
            event_name = event['name']['text']
            event_url = event.get('url', None)
            if self.keyword.lower() in event_name.lower():
                results.append(event_url)
        return results

    def get_end_time(self):
        return datetime.datetime.now() + \
            datetime.timedelta(minutes=self.watch_time)

    def send_sms(self, message):
        client = Client(
            self.twilio.get('account_sid', None),
            self.twilio.get('auth_token', None),
        )
        response = client.messages.create(
            to=self.twilio.get('to_number', None),
            from_=self.twilio.get('from_number', None),
            body=message,
        )
        return response

    def start_watching(self):
        results_found = 0
        end_time = self.get_end_time()
        while results_found < 3 and datetime.datetime.now() < end_time:
            results = self.check_eventbrite()
            if results:
                results_found += 1
            for result in results:
                self.send_sms(result)
            time.sleep(60)
