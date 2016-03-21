import json, requests

url = "https://www.govtrack.us/api/v2/vote"

params = dict(
    congress="112",
    chamber="house",
    session="2011",
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

ofile = open("/tmp/votes.out", 'w')

ofile.write("The meta is %s\n" % data["meta"])

for item in data["objects"]:
    ofile.write(" The vote number is %s\n" % item["number"]) 
    ofile.write(" The vote id is %s\n" % item["id"])
    ofile.write(" The options are %s\n" % item["options"])
    ofile.write(" The objects are %s\n" % item)
ofile.close()

#ofile = open("/tmp/representatives.out", 'w')

#ofile.write("The meta is %s\n" % data["meta"])

#ofile.close()
