import json, requests

url = "https://www.govtrack.us/api/v2/person/400054"

params = dict(
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

print "The data is %s" % data
