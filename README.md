# gam-events-stats

gam-events-stats is a tiny tool that attempts to fill in a gap left by [GAMADV-xtd3](https://github.com/taers232c/GAMADV-XTD3) which prevents users from querying on calendar events. This tool will return a list of attendees of a single event or a reccurring set of events, depending on their response to the event.

## Prerequisites

1. You need to install [GAMADV-xtd3](https://github.com/taers232c/GAMADV-XTD3) with enough scopes to run the calendar commands.

2. You need to know the email of one of recipients of the event.

3. You need to know the event ID or the recurring event ID of the event(s). An easy way to get it is to run the following:

```bash
gam calendar <email> show event
```
## Usage

```bash
python3 gamcalendar.py
```
