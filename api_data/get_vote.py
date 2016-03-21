import json, requests

url = "https://www.govtrack.us/api/v2/vote_voter"

params = dict(
    vote=1,
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

ofile = open("/tmp/vote.out", 'w')

ofile.write("The data is %s\n" % data)

ofile.close()

#ofile = open("/tmp/representatives.out", 'w')

#ofile.write("The meta is %s\n" % data["meta"])

#ofile.close()
