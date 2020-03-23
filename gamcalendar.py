"""gets the list of attendees of a recurring event"""

import json
import subprocess
import sys
from attendancecounter import count_attendance


def main():
    email = sys.argv[1]
    event_id = sys.argv[2]
    response_answer = sys.argv[3]

    process = subprocess.run(['gam', 'calendar', email, 'info', ' event', 'id', event_id,
                              'maxinstances', '0', 'fields', 'attendees', 'formatjson'],
                             stdout=subprocess.PIPE,
                             universal_newlines=True,
                             check=False)

    json_objects = str(process.stdout)

    calendar_list = []
    # parse JSON line by line
    for line in json_objects.splitlines():
        calendar_list.append(json.loads(line))

    count_attendance(calendar_list, response_answer)


if __name__ == '__main__':
    main()
