
from calendar_integration import create_google_calendar_link
from send_email import send_email, load_template
import config

def schedule_interview(candidate_name, candidate_email, interview_date, interview_time,):
    # googele calendar link generation  
    calendar_link = create_google_calendar_link(candidate_name, interview_date, interview_time)

    # email details setup for HR
    hr_replacements = {
        "candidate_name": candidate_name,
        "interview_date": interview_date,
        "interview_time": interview_time,
        "calendar_link": calendar_link
    }
    hr_email_body = load_template("templates/hr.html", hr_replacements)
    send_email(config.HR_MANAGER_EMAIL, "Interview Scheduled with Candidate", hr_email_body)

    # email details setup for Candidate
    candidate_replacements = {
        "candidate_name": candidate_name,
        "interview_date": interview_date,
        "interview_time": interview_time,
        "calendar_link": calendar_link
    }
    candidate_email_body = load_template("templates/candidate.html", candidate_replacements)
    send_email(candidate_email, "Interview Confirmation", candidate_email_body)

# test case details 
if __name__ == "__main__":
    schedule_interview("Siva Prakash", "abinesh.p.csd.2021@snsce.ac.in", "2024-11-15", "09:30")
