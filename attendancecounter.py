"""gets emails of the attendees and counts their attendance"""
import collections
import re


def count_attendance(cal_objs, response):
    email_list = []

    for each_record in cal_objs:
        for event_details in each_record['event']['attendees']:
            if ((event_details['responseStatus'] == response)
               and not (re.match(".*@resource.calendar.google.com", event_details['email']))):
                email_list.append(event_details['email'])

    accepted_freq = collections.Counter(email_list)
    accepted_freq = [list(i) for i in accepted_freq.items()]
    print(accepted_freq)
