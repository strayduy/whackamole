import json, requests

url = "https://www.govtrack.us/api/v2/vote/1"

params = dict(
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

ofile = open("/tmp/vote_meta.out", 'w')

ofile.write("The data is %s\n" % data)

ofile.close()

#ofile = open("/tmp/representatives.out", 'w')

#ofile.write("The meta is %s\n" % data["meta"])

#ofile.close()
