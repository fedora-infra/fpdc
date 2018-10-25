import openidc_client
import json
import os

oidc = openidc_client.OpenIDCClient(
    "fpdc",
    "https://iddev.fedorainfracloud.org/openidc/",
    {"Token": "Token", "Authorization": "Authorization"},
    os.getenv("OIDC_RP_CLIENT_ID"),
    os.getenv("OIDC_RP_CLIENT_SECRET"),
)

scopes = ["openid", "profile", "email", "https://id.fedoraproject.org/scope/groups"]

url = "http://localhost:8000/api/v1/release"

data = {
    "release_id": "fedora-29",
    "short": "f29",
    "version": 29,
    "name": "Fedora 29",
    "release_date": "2018-10-23",
    "eol_date": "2019-10-23",
    "sigkey": "dsfdsgdsgdsgsdg",
}

common_request_arguments = {
    "data": json.dumps(data),
    "headers": {"Content-Type": "application/json"},
    "timeout": 60,
    "http_method": "POST",
}
resp = oidc.send_request(scopes=scopes, url=url, **common_request_arguments)
print(resp.status_code)
