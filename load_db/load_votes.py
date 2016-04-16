import json
import os

senate_file = open("/tmp/votes/senate.json", 'w')

outcome_dict = {"No": "No",
                "Nay": "No",
                "Yea": "Yes",
                "Aye": "Yes",
                "Yes": "Yes",
                "Not Voting": "Abstain",
                "Present": "Abstain"}

for subdir, dirs, files in os.walk("rsync_data/votes"):
  for file_name in files:
    if not file_name.endswith(".json"):
      continue
    filepath = subdir + os.sep + file_name
    with open(filepath, 'r') as ifile:
      data = json.load(ifile)
      if data["category"] in ("quorum", "procedural", "leadership", "nomination", "cloture"):
        continue
      if "senate" in data["source_url"]:
        ofile = senate_file
      else:
        continue 
      if "title" not in data["bill"]:
        print "There is no title in %s" % filepath
      bill_title = data["bill"]["title"]
      bill_link = "https://www.govtrack.us/congress/votes/%s-%s/%s%s" % (
        data["congress"], data["session"], data["chamber"], data["number"])
      for outcome in ["No", "Nay", "Not Voting", "Present", "Yea", "Aye", "Yes"]:
        if outcome not in data["votes"]:
          continue
        for reps in data["votes"][outcome]:
          vote_dict = {"rep_state":reps["state"],
                       "rep_name":reps["display_name"],
                       "bill_title":bill_title,
                       "bill_link":bill_link,
                       "outcome":outcome_dict[outcome]}
          json.dump(vote_dict, ofile)
          ofile.write('\n')

senate_file.close()
