import google.auth
from google.auth.transport.requests import Request

credentials, project = google.auth.default()

credentials.refresh(Request())

print("Project:", project)
print("Service Account:", credentials.service_account_email)
