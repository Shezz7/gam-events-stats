import os
import json
import subprocess
import collections
from attendanceCounter import countAttendance
import sys

email = sys.argv[1]
event_id = sys.argv[2]
response_answer = sys.argv[3]

process = subprocess.run(['gam','calendar',email,'info','event','id',event_id,'maxinstances','0','fields','attendees','formatjson'
 ],
                          stdout=subprocess.PIPE,
                          universal_newlines=True)
# collection of multiple JSON objects
json_collection=str(process.stdout)

calendar_list=[]
# parse JSON line by line
for line in json_collection.splitlines():
      calendar_list.append(json.loads(line))

countAttendance(calendar_list,response_answer)