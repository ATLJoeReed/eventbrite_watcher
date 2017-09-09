# eventbrite_watcher
Process to watch Eventbrite for new event(s) by a specified organization. You will need to get an OAuth token from Eventbrite as well as Twilio credentials and sms number. To get this setup on your machine follow the below steps.

- Step #1: Clone this repo to your machine and run pip install -r requirements.txt.
- Step #2: You will need to create a directory "config" and have the file settings.py in it. This file will contains: 
      
      - BASE_URL - which is currently "https://www.eventbriteapi.com/v3/events/search/" 
      
      - OAUTH_TOKEN - this is the oauth token you will get from Eventbrite to access their API.
      
      - TWILIO - this is a dictionary that contains your account_sid, auth_token, from_number (these are from twilio) and to_number which is who is getting the text message when a specific event is found.

- Step #3: You can then adjust the runner.py to watch a specific organization for a specific event(s) that contain a keyword you are looking for.

watcher = EventbriteWatcher(540, '6453217513', 'made') - This example is watching for 9 hours (540 minutes) the organization Switchyards for a event(s) that contain "made" in the description. I have this hosted on PythonAnywhere and it fires in the morning and runs for 9 hours sleeping 10 minutes between checks. 

More specifically I want to get a text when Switchyards posts the event for Made in Atlanta. The first 100 registrants get a free t-shirt. 
