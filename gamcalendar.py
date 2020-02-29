import os
import json
import subprocess
import collections
from attendanceCounter import countAttendance

email=input("Enter the email of any one recipient who has received an invitation to the event: ")
response_answer=input("Enter the response filter(accepted/declined/needsAction): ")
event_id=input("Enter the event ID of the event: ")
process = subprocess.run(['gam','calendar',email,'info','event','id',event_id,'maxinstances','0','fields','attendees','formatjson'
],
                         stdout=subprocess.PIPE,
                         universal_newlines=True)
json_collection=str(process.stdout)                                         #collection of multiple JSON objects

calendar_list=[]

for line in json_collection.splitlines():                                   #parse JSON line by line
     calendar_list.append(json.loads(line))

countAttendance(calendar_list,response_answer)