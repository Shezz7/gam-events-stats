import collections

def countAttendance(cal_objs,response):
    i=0
    email_list=[]

    for each_record in cal_objs:
        for event_details in each_record['event']['attendees']:
            if event_details['responseStatus']==response:
                email_list.append(event_details['email'])                   # list of all emails matched

    accepted_freq=collections.Counter(email_list)                           # Counter object of emails and frequencies
    accepted_freq = [list(i) for i in accepted_freq.items()]                # Convert counter to list
    print(accepted_freq)