import os

# 1. Change the API_KEY and STUDENT_ID to your own.
# 2. You must change service_account_key.json to the root of the project!
API_KEY = "AIzaSyARSGPsO_7GP8xTK_HNotIDrfAzrZ5kYZM"
STUDENT_ID = "86765600724124" \
    if os.environ.get('STUDENT_ID') is None else os.environ.get('STUDENT_ID')

API_ENDPOINT = 'https://gateway-3y3heh3w.ue.gateway.dev'
LOCATIONS = "asia-east2"
