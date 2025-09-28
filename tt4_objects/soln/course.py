import json
import dateutil.parser


class Assignment(object):
    """
    Represents an assignment in the course.

    See constructor for description of attributes.
    """

    def __init__(self, assignment_id, deadline):
        """
        Constructor

        Parameters:
        - assignment_id: (string) An identifier for the assignment
        - deadline: (datetime) The assignment's deadline
        """

        self.assignment_id = assignment_id
        self.deadline = deadline


class Student(object):
    """
    Represents a student in the course.

    See constructor for description of attributes.
    """

    def __init__(self, cnetid, first_name, last_name, dropped):
        """
        Constructor

        Parameters:
        - cnetid: (string) The student's CNetID
        - first_name, last_name: (string) The student's first and last name.
        - dropped: (boolean) Whether the student dropped this class.
        """

        self.cnetid = cnetid
        self.first_name = first_name
        self.last_name = last_name
        self.dropped = dropped


class Team(object):
    """
    Represents a team in the course. 

    A Team object has the following composition relationships:

    - Has one or more Student objects associated with it. These
      are the members of the team.
    - Has zero or more Submission objects associated with it.
      These are the submissions made by the team.
    """

    def __init__(self, team_id, students):
        """
        Constructor

        Parameters:
        - team_id: (string) The team's identifier.
        - students: (list of Student) The students in the team.
        """
        self.team_id = team_id
        self.students = students
        self.submissions = []

    def add_submission(self, assignment, submitted_at, extensions_used):
        s = Submission(self, assignment, submitted_at, extensions_used)
        self.submissions.append(s)

    @property
    def includes_dropped(self):
        for s in self.students:
            if s.dropped:
                return True
        return False


class Submission(object):
    """
    Represents a single submission by a team. 

    A Submission object has the following composition relationships:

    - Has a Team object associated with it (the team making the submission)
    - Has an Assignment object associated with it (the assignment for
      which this submission is being made)
    """

    def __init__(self, team, assignment, submitted_at, extensions_used):
        """
        Constructor

        Parameters:
        - team: (Team) The team making the submission.
        - assignment: (Assignment) The assignment for which the submission
          is being made.
        - submitted_at: (datetime) The time at which the submission was made
        - extensions_used: (int) The number of extensions used in this submission.
        """
        self.team = team
        self.assignment = assignment
        self.submitted_at = submitted_at
        self.extensions_used = extensions_used

    @property
    def deadline_delta(self):
        delta = self.submitted_at - self.assignment.deadline
        return int(delta.total_seconds())


def time_str(t):
    """
    Converts a time in seconds to a string representation
    in days, hours, minutes, seconds.

    Parameters:
    - t: (integer) A time in seconds

    Returns: (string) A string representation.
    """
    MINUTE = 60
    HOUR = 60 * MINUTE
    DAY = 24 * HOUR
    
    t = int(t)
    days = t // DAY
    hours = (t % DAY) // HOUR
    minutes = (t % HOUR) // MINUTE
    seconds = t % MINUTE

    if days == 0:
        return "{}h {}m {}s".format(hours, minutes, seconds)
    else:
        return "{}d {}h {}m {}s".format(days, hours, minutes, seconds)


def load_data(assignments_file, students_file, teams_file):
    """
    Loads the course data from the JSON files.

    An assignment is represented as a dictionary:

      {
        "assignment_id": "pa1", 
        "deadline": "2017-01-10T02:00:00+00:00"
      }

    A student is represented as a dictionary:

      {
        "first_name": "Cliff", 
        "last_name": "Nixon", 
        "cnetid": "cnixon", 
        "dropped": false
      }

    A team is represented as a dictionary (note that it contains
    a list of submissions, also represented as dictionaries):

      {
        "students": [
          "jdunlap", 
          "ghood"
        ], 
        "team_id": "jdunlap-ghood", 
        "submissions": [
          {
            "assignment_id": "pa2", 
            "submitted_at": "2017-01-18 00:27:35.886530+00:00", 
            "extensions_used": 0
          }, 
          {
            "assignment_id": "pa3", 
            "submitted_at": "2017-01-24 02:00:11.428773+00:00", 
            "extensions_used": 0
          }
        ]
      }

    Note: When loading the data, this function will convert the
    "deadline" field (in assignments) and the "submitted_at" field
    (in submissions in teams) to Python's datetime type.


    Parameter:
    - assignments_file: (string) Path of assignments file
    - students_file: (string) Path of assignments file
    - teams_file: (string) Path of assignments file

    Returns a tuple with three values:
    - A list of assignment dictionaries
    - A list of student dictionaries
    - A list of team dictionaries
    
    """

    with open(assignments_file) as f:
        assignments_json = json.load(f)
        for a in assignments_json:
            a["deadline"] = dateutil.parser.parse(a["deadline"])

    with open(students_file) as f:
        students_json = json.load(f)

    with open(teams_file) as f:
        teams_json = json.load(f)
        for t in teams_json:
            for s in t["submissions"]:
                s["submitted_at"] = dateutil.parser.parse(s["submitted_at"])

    return assignments_json, students_json, teams_json


def create_assignment_objects(assignments_json):
    """
    Creates Assignment objects from the loaded dataset.

    Parameters:
    - assignments_json: A list of assignment dictionaries, as
      returned by load_data

    Returns: Dictionary mapping assignment identifiers to 
             Assignment objects.
    """    
    assignments = {}
    
    for a in assignments_json:
        a_obj = Assignment(a["assignment_id"], a["deadline"])
        assignments[a["assignment_id"]] = a_obj

    return assignments


def create_student_objects(students_json):
    """
    Creates Student objects from the loaded dataset.

    Parameters:
    - students_json: A list of student dictionaries, as
      returned by load_data

    Returns: Dictionary mapping CNetIDs to Student objects.
    """    
    students = {}

    for s in students_json:
        s_obj = Student(s["cnetid"], s["first_name"], s["last_name"], s["dropped"])
        students[s["cnetid"]] = s_obj

    return students


def create_team_objects(teams_json, students, assignments):
    """
    Creates Team objects from the loaded dataset.

    Parameters:
    - teams_json: A list of team dictionaries, as
      returned by load_data

    Returns: Dictionary mapping team identifiers to Team objects.
    """    
    teams = {}

    for t in teams_json:
        team_students = [students[s] for s in t["students"]]
        t_obj = Team(t["team_id"], team_students)
        teams[t["team_id"]] = t_obj

        # Add submissions to team  
        for s in t["submissions"]:
            a = assignments[s["assignment_id"]]
            t_obj.add_submission(a, s["submitted_at"], s["extensions_used"])

    return teams


if __name__ == "__main__":
    assignments_json, students_json, teams_json = load_data("data/assignments.json",
                                                            "data/students.json",
                                                            "data/teams.json")

    assignments = create_assignment_objects(assignments_json)
    students = create_student_objects(students_json)
    teams = create_team_objects(teams_json, students, assignments)

    # Count the number of teams where one of the team members ended
    # up dropping the class
    teams_with_dropped = 0
    for t in teams.values():
        if t.includes_dropped:
            teams_with_dropped += 1
    print("The number of teams with dropped students is {}".format(teams_with_dropped))

    print()

    # For non-late submissions, how many seconds before the deadline
    # do teams submit their assignments (on average)
    deltas = []
    for t in teams.values():
        for s in t.submissions:
            d = s.deadline_delta
            if d < 0:
                deltas.append(-d)

    if len(deltas) > 0:
        avg_delta = sum(deltas) / len(deltas)
        avgs = time_str(avg_delta)

        print("On average, non-late submissions are made", avgs, "before the deadline")
        








