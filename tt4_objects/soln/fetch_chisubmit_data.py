import names
import random
import json

from chisubmit.client import Chisubmit

random.seed("lab5objects")

c = Chisubmit("...", "https://chisubmit-backend.cs.uchicago.edu/api/v1/", ssl_verify=False)

chisubmit_course = c.get_course("cs233-win-17")

chisubmit_assignments = chisubmit_course.get_assignments()
chisubmit_students = chisubmit_course.get_students()
chisubmit_teams = chisubmit_course.get_teams()

chisubmit_teams_submissions = {}
for t in chisubmit_teams:
    chisubmit_teams_submissions[t.team_id] = t.get_assignment_registrations()

# Anonymize assignments

assignment_real_to_alias = {"p1a": "pa1", "p1b": "pa2", "p1c": "pa3",
                            "p2a": "pa4", "p2b": "pa5",
                            "p3": "pa6"}

assignments = []
for a in chisubmit_assignments:
    assignments.append( {"assignment_id": assignment_real_to_alias[a.assignment_id], 
                         "deadline": a.deadline.isoformat()} )

with open("data/assignments.json", "w") as f:
    json.dump(assignments, f, indent=2)

# Anonymize students
student_real_to_alias = {}
students = {}
for s in chisubmit_students:
    while True:
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        cnetid = (first_name[0] + last_name).lower()
        if cnetid not in students:
            student_real_to_alias[s.username] = cnetid
            students[cnetid] = {"cnetid": cnetid, 
                                "first_name": first_name,
                                "last_name": last_name,
                                "dropped": s.dropped}
            break

with open("data/students.json", "w") as f:
    json.dump(students.values(), f, indent=2)


# Anonymize teams
team_real_to_alias = {}
teams = {}
for t in chisubmit_teams:
    team_students = t.team_id.split("-")
    team_students_alias = [student_real_to_alias[s] for s in team_students]
    alias = "-".join(team_students_alias)
    team_real_to_alias[t.team_id] = alias
    teams[alias] = {"team_id": alias,
                    "students": team_students_alias,
                    "submissions": []}

# Anonymize submissions
for team_id, submissions  in chisubmit_teams_submissions.items():
    team_alias = team_real_to_alias[team_id]
    for s in submissions:
        if s.final_submission is not None:
            assignment_alias = assignment_real_to_alias[s.assignment_id]
            sd = {"assignment_id": assignment_alias,
                  "submitted_at": s.final_submission.submitted_at.isoformat(" "),
                  "extensions_used": s.final_submission.extensions_used}
            teams[team_alias]["submissions"].append(sd)


with open("data/teams.json", "w") as f:
    json.dump(teams.values(), f, indent=2)


