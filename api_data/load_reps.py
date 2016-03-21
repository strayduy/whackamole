import json, requests

url = "https://www.govtrack.us/api/v2/role"

params = dict(
    current='true',
    role_type='representative',
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

ofile = open("/tmp/representatives.out", 'w')

ofile.write("The meta is %s\n" % data["meta"])

for item in data["objects"]:
    ofile.write("The state and district are %s and %s\n" % (item["state"], item["district"])) 
    ofile.write(" The id is %s, the name is %s %s\n" % (item["id"], item["person"]["firstname"].encode('utf8'), item["person"]["lastname"].encode('utf8')))
    ofile.write(" The phone is %s\n" % item["phone"])
    ofile.write(" The website is %s\n" % item["website"])

ofile.close()
