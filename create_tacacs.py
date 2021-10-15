from ciscoisesdk import IdentityServicesEngineAPI
from ciscoisesdk.exceptions import ApiError
from dotenv import load_dotenv
import os
from pprint import pprint as ppr

load_dotenv()
admin = os.getenv("ISE_ADMIN")
pw = os.getenv("ISE_PW")
base_url = os.getenv("ISE_URL")

api = IdentityServicesEngineAPI(
    username=admin, password=pw, base_url=base_url, version="3.0.0", verify=False)


print("=" * 50)
# Get Admin Users
search_result = api.admin_user.get_all()
ppr(search_result.response)

print("=" * 50)

# Get All TACACS Users
search_result = api.tacacs_profile.get_all()
ppr(search_result.response)
print("=" * 50)
