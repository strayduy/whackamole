import json, requests

url = "https://www.govtrack.us/api/v2/vote_voter"

params = dict(
    person="400222",
    limit="6000",
    order_by="created",
    format="csv",
    fields="vote__id,created,option__value,vote__category,vote__chamber,vote__question,vote__number",
)

resp = requests.get(url=url, params=params)

ofile = open("/tmp/rep_votes.csv", 'w')

ofile.write(resp.text.encode('utf8'))

ofile.close()
