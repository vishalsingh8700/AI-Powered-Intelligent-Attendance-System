import os
from urllib.parse import parse_qs, urlparse

import httpx
import streamlit as st
from supabase import ClientOptions, create_client

# Force environment to ignore SSL at the system level for this session
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['SSL_CERT_FILE'] = ''

# Get your credentials from secrets
raw_url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

# Normalize the Supabase URL in case the secret contains the management portal URL
# Example bad URL: https://mcp.supabase.com/mcp?project_ref=cyhcrgumjmjzwmzyncha
parsed = urlparse(raw_url)
if parsed.netloc == "mcp.supabase.com" and parsed.path.startswith("/mcp"):
    project_ref = parse_qs(parsed.query).get("project_ref", [None])[0]
    if project_ref:
        url = f"https://{project_ref}.supabase.co"
    else:
        url = raw_url
else:
    url = raw_url

# Create a custom httpx client that bypasses SSL verification
# This is necessary when corporate network certificates break SSL validation.
verify_bypass_client = httpx.Client(verify=False)

# Initialize Supabase with the custom httpx client via ClientOptions
supabase = create_client(
    url,
    key,
    options=ClientOptions(httpx_client=verify_bypass_client),
)
