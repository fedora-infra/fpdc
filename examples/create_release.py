from fpdc_client import FPDC, Release

server = FPDC(url="http://localhost:8000")
server.connect()

# Use oidc-register to get a client_secret.json file
server.login(auth_file="client_secrets.json")
new_release = Release.create(
    {
        "release_id": "fedora-42",
        "short": "f42",
        "version": "42",
        "name": "Fedora",
        "release_date": "2042-01-01",
        "eol_date": "2042-12-31",
        "sigkey": "towel",
    }
)

releases = Release.all()
for release in releases:
    print(release)
