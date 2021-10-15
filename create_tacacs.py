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

resp = api.allowed_protocols.get_all()


ppr(resp)
