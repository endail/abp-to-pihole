import requests
from abp.filters import parse_filterlist
from abp.filters.parser import Filter

MASTER_LIST = "https://api.github.com/repos/AdguardTeam/cname-trackers/contents/trackers?ref=master"

## get urls of txt files containing abp lists
def getLists():
        resp = requests.get(MASTER_LIST)
        txtUrls = (f["download_url"] for f in resp.json() if f["name"].endswith(".txt"))
        return list(txtUrls)

for l in getLists():
	for line in parse_filterlist(requests.get(l).text.splitlines()):
		if isinstance(line, Filter):
			print(line.text[2:-1])