# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://vinayprasadg.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0rkd6LUx0UQlHLNUMpdUjRNlC0EXTqcL4SrURd4OSGiEteO6CTK1n4Mr5RLtsHgjOQoWzr8553TzJsEFSqit3KutPFZPwSJHrP54K1lhMv5zeHb4htthrueXNWvfskNu08YH4YrodKCcFah0KwYj1-BoFULrCMaUVCBN6hLFzJBk=01863F66"

auth = HTTPBasicAuth("gvinayprasad12@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)