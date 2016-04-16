import json
import os

senate_votes_file = open("/tmp/votes/senate.json", 'w')
senate_reps_file = open("/tmp/reps/senate.json", 'w')

outcome_dict = {"No": "No",
                "Nay": "No",
                "Yea": "Yes",
                "Aye": "Yes",
                "Yes": "Yes",
                "Not Voting": "Abstain",
                "Present": "Abstain"}

class SenateRep(object):

  rep_type = "senator"

  def __init__(self, display_name, state):
    self.display_name = display_name
    self.state = state
    self.yes_votes = 0
    self.no_votes = 0
    self.abstain_votes = 0

  def increment_vote(self, vote):
    if vote == "Yes":
      self.yes_votes += 1
    elif vote == "No":
      self.no_votes += 1
    elif vote == "Abstain":
      self.abstain_votes += 1

  def __repr__(self):
    return "%s, %s, votes [yes, no, abstain]: %s" % (
      self.display_name, self.state, self.votes)

# Stores a dictionary from representative's id to their object
reps_dict = {}

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
        votes_ofile = senate_votes_file
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
                       "rep_id": reps["id"],
                       "bill_title":bill_title,
                       "bill_link":bill_link,
                       "outcome":outcome_dict[outcome]}
          json.dump(vote_dict, votes_ofile)
          votes_ofile.write('\n')
          if reps["id"] not in reps_dict:
            reps_dict[reps["id"]] = SenateRep(reps["display_name"], reps["state"])
          reps_dict[reps["id"]].increment_vote(outcome_dict[outcome])

for rep_id, rep in reps_dict.iteritems():
  d = {"rep_id":rep_id,
       "rep_name":rep.display_name,
       "state":rep.state,
       "yes_votes":rep.yes_votes,
       "no_votes":rep.no_votes,
       "abstain_votes":rep.abstain_votes}
  json.dump(d, senate_reps_file)
  senate_reps_file.write('\n')

senate_votes_file.close()
senate_reps_file.close()
