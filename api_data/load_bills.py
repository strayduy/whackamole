import json, requests

url = "https://www.govtrack.us/api/v2/bill?congress=112&order_by=-current_status_date"

params = dict(
)

resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

ofile = open("/tmp/bills.out", 'w')

ofile.write("The meta is %s\n" % data["meta"])

for item in data["objects"]:
    ofile.write("The bill number is %s\n" % item["number"]) 
    ofile.write(" The bill title is %s\n" % item["titles"][0][2])

ofile.close()

#ofile = open("/tmp/representatives.out", 'w')

#ofile.write("The meta is %s\n" % data["meta"])

#ofile.close()
