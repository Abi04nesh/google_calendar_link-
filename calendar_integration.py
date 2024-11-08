
from datetime import datetime, timedelta
import urllib.parse

def create_google_calendar_link(candidate_name, interview_date, interview_time, duration_minutes=30, location="Online"):
    start_dt = datetime.strptime(f"{interview_date} {interview_time}", "%Y-%m-%d %H:%M")
    end_dt = start_dt + timedelta(minutes=duration_minutes)
    
    # Format dates in ISO 8601 for Google Calendar
    start_str = start_dt.strftime("%Y%m%dT%H%M%SZ")
    end_str = end_dt.strftime("%Y%m%dT%H%M%SZ")
    
    event_title = f"Interview with {candidate_name}"
    details = f"Interview scheduled with {candidate_name} on {interview_date} at {interview_time}."
    
    # Generate Google Calendar URL
    google_calendar_url = (
        "https://calendar.google.com/calendar/render?action=TEMPLATE"
        f"&text={urllib.parse.quote(event_title)}"
        f"&dates={start_str}/{end_str}"
        f"&details={urllib.parse.quote(details)}"
        f"&location={urllib.parse.quote(location)}"
        "&trp=true"
    )
    
    return google_calendar_url
