# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://vinayprasadg.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0rkd6LUx0UQlHLNUMpdUjRNlC0EXTqcL4SrURd4OSGiEteO6CTK1n4Mr5RLtsHgjOQoWzr8553TzJsEFSqit3KutPFZPwSJHrP54K1lhMv5zeHb4htthrueXNWvfskNu08YH4YrodKCcFah0KwYj1-BoFULrCMaUVCBN6hLFzJBk=01863F66"

auth = HTTPBasicAuth("gvinayprasad12@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "Vinay's first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "VIN"
    },
    "issuetype": {
      "id": "10003"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))